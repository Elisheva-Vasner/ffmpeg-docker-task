# Docker FFmpeg Task

This repository contains a Dockerfile that sets up a container with ffmpeg installed.

# What's Inside

Uses ubuntu:20.04 as the base image
Installs ffmpeg using apt
Sets ffmpeg as the container's default entrypoint

# why ubuntu? 
simpel and well supports by - ffmpeg

# what is ffmpeg

its oftenly used for:
converting videos
changes your video or audio size
Take the sound out of a video and save it as an audio

## exampel usage
ffmpeg -i input.mp4 output.mp3

