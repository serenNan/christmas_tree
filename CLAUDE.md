# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Interactive 3D Christmas tree visualization with photo memories. Uses Three.js for WebGL rendering and MediaPipe for hand gesture recognition to control display modes.

## Technology Stack

- **Three.js** (v0.160.0): 3D rendering, post-processing (UnrealBloomPass), particle systems
- **MediaPipe Hands**: Real-time hand gesture detection via webcam
- **Tailwind CSS**: UI styling (loaded via CDN)
- **Pure HTML/JS**: No build system, files run directly in browser

## Architecture

Each HTML file is a self-contained single-page app with different feature sets:

| File | Features |
|------|----------|
| `1_tree.html` | Full featured: spiral particles, snowfall, photo upload, gesture control, keyboard shortcuts |
| `2_tree.html` | Mobile-compatible: touch interactions, snapshot export, OrbitControls, error handling |
| `3_tree.html` | Alternative UI: sidebar controls, galaxy mode for photos, older MediaPipe API |
| `4_tree.html` | Same as 1_tree.html (appears to be a duplicate) |

## Key Systems

### Display Modes (STATE.mode)
- `TREE`: Particles form Christmas tree shape, auto-rotation
- `SCATTER`: Particles explode into 3D sphere
- `FOCUS`: Selected photo enlarges to center

### Gesture Detection
Hand gestures trigger mode changes:
- Pinch (thumb+index close) → FOCUS mode
- Closed fist (avgDist < 0.25) → TREE mode
- Open palm (avgDist > 0.4) → SCATTER mode

### Particle Types
Decorations rendered via Three.js meshes: BOX (green), GOLD_STAR, GOLD_SPHERE, RED (spheres), CANE (candy canes), DUST, PHOTO (uploaded images with gold frames)

## Development

Open any HTML file directly in a modern browser. No build or install required.

**Requirements:** WebGL support, webcam access for gesture features

**Keyboard:** Press 'H' to toggle UI visibility (1_tree.html, 4_tree.html)
