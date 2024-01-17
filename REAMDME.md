# Mosaic Motif - Mosaic Browsing

Hi there. This is an attempt to create a visual representation for the **Mosaic Browsing** problem from the ICPC. For the problem statement - [45th ICPC World Finals - Problem G - PDF page 13](https://icpc.global/worldfinals/problems/icpc2021.pdf)

## Demo video

[video demo](mosaic-browsing.mp4)

## Info

I have used Python to create a GUI with PySimpleGUI library and a naive approach to solving the Mosaic Browsing problem (yeah, general nested looping - bad $O(n^2)$ time complexity, for a better approach, see the video solutions on YouTube that use a Fast Forier Transform and String Pattern Matching techniques). The main idea is to try and make a GUI to visually look at the matches.

## Codeview

**Language Used**: 🐍 Python

**Libraries Used**:

* **PySimpleGUI** - For creating windows, buttons, input fieds and other GUI elements
* **OpenCV** - For drawing images of mosaic and motif, highlighting regions
