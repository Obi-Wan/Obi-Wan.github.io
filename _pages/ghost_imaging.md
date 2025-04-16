---
title: "Ghost Imaging"
permalink: /ghost_imaging/
layout: single

classes: wide
toc: true
toc_label: "Sections:"
tags: [ghost-imaging, hard x-ray, x-ray fluorescence, XRF-GI]
---

## What is Ghost Imaging?

Ghost imaging (GI) is a technique used in optics and imaging science that allows
for the reconstruction of an image from a light source that has never directly
interacted with the object being imaged.
In a typical setup, a structured light source is used to illuminate an object,
and the light that interacts with the object is collected and detected by a non
spatially resolving detector.
Simultaneously, an image of the structured light source is recorded with detector
array, such as a CCD camera (spatially resolving).
We focus on X-rays, for which these structured beams are usually obtained by
inserting non-configurable transversely-displaced structuring masks in the beam,
to encode the spatial information in the acquired GI signals.

## Why is ghost imaging so interesting?

Ghost imaging (GI) presents a few attractive advantages.

**Tradeoff Between Resolution, Measuring Time, and Dose**: GI offers a tradeoff between resolution, measuring time, and dose. This makes it particularly useful for applications where minimizing radiation exposure or acquisition time is critical.

**High Compression and Efficiency**: GI can achieve high compression rates (e.g., 10x or 20x), meaning it requires significantly fewer realizations compared to the number of pixels. This results in faster and lower-dose acquisitions, enhancing efficiency and reducing potential damage to samples.

**Resolving Scattering Signals**: GI enables the resolution of scattering signals without the need for focusing the beam, which could become technically challenging, or using collimators, which often waste a significant portion of the emitted photons.

**Tracking Sample Drifts**: By illuminating larger regions of the sample at once, GI allows for the tracking of sample drifts during acquisition. This is a significant advantage over traditional imaging techniques, such as X-ray fluorescence (XRF) imaging, where we only illuminate a point-like region of the sample at a time.

**Enhanced Resolution**: GI can push the resolution of imaging techniques beyond the limits imposed by the focus or pixel size of conventional detectors.

## X-ray fluorescence ghost imaging

We have recently developed synchrotron-based X-ray fluorescence GI (XRF-GI)
<a href="/publications/#J15">[J15]</a>.
XRF imaging is usually achieved by scanning the samples with a focused beam
(pencil beam, PB), and by collecting the emitted XRF signal (spectrum) with
single-pixel energy-resolving detectors.

<div style="text-align: center;">
  <div style="display: inline-block; text-align: center; width: 45%; margin: 0 1.25%;">
    <img src="../assets/images/XRF-PB.png" alt="Figure 1a" style="width: 100%;">
    <br>
    <p>(a) Pencil Beam</p>
  </div>
  <div style="display: inline-block; text-align: center; width: 45%; margin: 0 1.25%;">
    <img src="../assets/images/XRF-GI.png" alt="Figure 1b" style="width: 100%;">
    <br>
    <p>(b) Ghost Imaging</p>
  </div>
  <p>
    <b>Figure 1:</b> X-ray fluorescence imaging modalities: (a) Pencil Beam scan; (b) Ghost Imaging.
  </p>
</div>

In the specific case of XRF-GI, an XRF detector records the spectrum associated
with each illumination pattern.
The XRF energy emission lines corresponding to different chemical elements are
reconstructed into spatially resolved maps, using computational imaging algorithms.
GI acquires spatial information on the whole FoV at each realization.
Thanks to the inherent compressibility of natural images, it is possible to acquire
fewer realizations than the number of pixels in the reconstructed image,
leading to reduced dose deposition, which is not possible with PB scans.

For more information, please visit the dedicated page on the subject: [Synchrotron-based X-ray Fluorescence Ghost Imaging](xrf-gi/).