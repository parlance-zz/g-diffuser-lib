import cv2
import glob
import numpy as np

from g_diffuser_config import DEFAULT_PATHS
from extensions import g_diffuser_utilities as gdu

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# this is the folder relative to the output path where the keyframes are stored
frames_path = "coolzoom"
expand_top = 50      # **the expand values here should match the values used to create the frames**
expand_bottom = 50   # these values are in % of the original image size
expand_left = 50
expand_right = 50
expand_softness = 80.
expand_space = 1.
start_in_black_void = True    # enabled to start zooming out from a black void instead of starting on the first frame
num_interpolated_frames = 90  # number of interpolated frames per keyframe
frame_rate = 60               # fps of the output videos
output_file = "zoom.mp4"      # name of output file to save in ./outputs
preview_output = False        # if enabled this will show a preview of the video in a window as it renders


# find keyframes and sort them
frame_filenames = sorted(glob.glob(DEFAULT_PATHS.outputs+"/"+frames_path+"/*.png"), reverse=True)
num_keyframes = len(frame_filenames)
frame0_cv2_image = cv2.imread(frame_filenames[0])
source_size = (int(frame0_cv2_image.shape[1]), int(frame0_cv2_image.shape[0]))
video_size = (source_size[0]*2, source_size[1]*2)

# setup opengl for compositing via pygame
pygame.init()
pygame.display.set_mode(video_size, HIDDEN|DOUBLEBUF|OPENGL, vsync=0)
gluOrtho2D(-1., 1., -1., 1.)
glDisable(GL_CULL_FACE); glDisable(GL_DEPTH_TEST)
glEnable(GL_TEXTURE_2D); glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

# load keyframes and generate blending masks
frame_textures = []
for f in range(num_keyframes):
    print("Generating textures {0}/{1}...".format(f+1, num_keyframes))
    cv2_image = cv2.imread(frame_filenames[f])
    np_image = gdl.expand_image(cv2_image, expand_top, expand_right, expand_bottom, expand_left, expand_softness, expand_space)
    frame_textures.append(glGenTextures(1))
    glBindTexture(GL_TEXTURE_2D, frame_textures[f])
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_LOD_BIAS, -1.4)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, np_image.shape[1], np_image.shape[0], 0, GL_RGBA, GL_UNSIGNED_BYTE, np_image)
    glGenerateMipmap(GL_TEXTURE_2D)

# create video encoder
video_output_path = DEFAULT_PATHS.outputs+"/"+gdl.get_noclobber_checked_path(DEFAULT_PATHS.outputs, frames_path+"/"+output_file)
print("Creating video of size {0}x{1}...".format(video_size[0], video_size[1]))
result = cv2.VideoWriter(video_output_path, cv2.VideoWriter_fourcc(*'H265'), frame_rate, video_size)
frame_pixels = (GLubyte * (4*video_size[0]*video_size[1]))(0)

if preview_output: # show video window if preview is enabled
    pygame.display.set_mode(video_size, SHOWN|DOUBLEBUF|OPENGL, vsync=0)

if start_in_black_void: start_offset = -5 # start by zooming in from a black screen if enabled
else: start_offset = 0 # otherwise start on the first keyframe

try:
    for f in range(start_offset, num_keyframes-1):
        print("Rendering {0}/{1}...".format(f+1, num_keyframes-1))

        for i in range(num_interpolated_frames):
            t = f + i/num_interpolated_frames

            glClear(GL_COLOR_BUFFER_BIT)

            start_frame = int(np.clip(t+0.5-6., 0, num_keyframes-1))
            end_frame = int(np.clip(t+0.5+6., 1, num_keyframes))
            for f0 in range(start_frame, end_frame):
                z = f0 - t + 1.
                scaleX = ((expand_left + expand_right)/100. +1.) ** (-z)
                scaleY = ((expand_top + expand_bottom)/100. +1.) ** (-z)

                glBindTexture(GL_TEXTURE_2D, frame_textures[f0])
                glPushMatrix()
                glScalef(scaleX, scaleY, 1.)
                glBegin(GL_QUADS)
                glTexCoord2f(0., 0.); glVertex2f(-1.,-1.)
                glTexCoord2f(1., 0.); glVertex2f( 1.,-1.)
                glTexCoord2f(1., 1.); glVertex2f( 1., 1.)
                glTexCoord2f(0., 1.); glVertex2f(-1., 1.)
                glEnd()
                glPopMatrix()

            glReadPixels(0, 0, video_size[0], video_size[1], GL_RGBA, GL_UNSIGNED_BYTE, frame_pixels)
            np_frame = np.array(frame_pixels).reshape(video_size[1], video_size[0], 4)
            result.write(np_frame)

            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    raise Exception("Operation cancelled by user")

except Exception as e:
    print("Error: {0}".format(str(e)))
    pygame.quit()
    raise

pygame.quit()

for i in range(frame_rate*3): # linger on the last frame for 3 seconds
    result.write(np_frame)

result.release()
print("Saved {0}".format(video_output_path))