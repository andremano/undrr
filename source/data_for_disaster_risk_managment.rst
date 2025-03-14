================================
Data for Disaster Risk Managment
================================

.. important:: Session objectives

   After this session you should be able to:

   + Recognize the variety of spatial data available for risk assessment and how different hazards require specific spatial, spectral, and temporal characteristics. Assess these characteristics across data types while considering additional constraints that impact data selection;
   + Where to search for and obtain some key datasets;
   + Evaluate the quality of a dataset with regards to its suitability for a purpose;
   + Understand what data sovereignty is and why it is important.

What is Spatial data?
---------------------

In geoinformatics, also called geoinformation science, we use the term **spatial data** to describe any type of data that can be linked to a geographic place, usually via coordinates. This means that spatial data has an **unambiguous location** (i.e. it can be associated to a specific location on the Planet). The classic data type is a map, a more modern one could be a satellite image (for an introduction on remote sensing see box). However, we need to consider that our work is largely done digitally on a computer, and that we might want to use data that are actually quite variable in nature. When we think about disasters or risk, we may want to include:

+ Tabular data or statistics (e.g. on the number of hazard or disaster events of a certain type and in a given time period);
+ Thematic data (e.g. a road or river network, soil types, or digital elevation models [DEMs]);
+ Topographic maps;
+ Model results (e.g. for flood hazard or slope instability);
+ Images (e.g. aerial photos or satellite images).
+ Point cloud data (LIDAR and laser scans)

In the next section we will take a closer look into different types of data.

Main types of data
==================

First, it is important to distinguish between *data type* and *data format*. The first usually refers to the nature of the data, that is what type of information is the data documenting, while the latter describes what type of computer file are you talking about, including technical specifications.

Regardless of the type and format, *data acquisition* is done through the use sensors, surveys and other methods, after which *data processing* follows in order to distil useful information. We will not do an exhaustive list of data acquisition and processing methods, still, :numref:`data_type_data_format` provides an overview of the most relevant data types for Disaster Risk Management.

.. _data_type_data_format:
.. figure:: _static/figures/data_for_disaster_risk_managment/data_type_data_format.png
      :alt: Overview of the main data types
      :figclass: align

      Overview of the main data types

For example, you might find statistics presented in a table with either coordinates or grouped per administrative area, or illustrated as a chart or graphic. It can also happen that field photographs are available. Associating those with the other data, and integrating the information you think is useful in those photos with the rest of the analysis, can be challenging. Also consider that many maps or aerial photographs are available only as paper hardcopies. To use them in our work we first have to convert them to a digital format. This can be done by digitizing relevant information, or by scanning and subsequently georeferencing the maps or images.

Some of the data types mentioned in the diagram of :numref:`data_type_data_format` deserve a closer look due to their importance for Disaster Risk Management. Among all the data types, those acquired through **remote sensing** deserve especial attention - if you want to dive a bit more into what exactly it is remote sensing, we invite you to expand the *What is remote sensing* dropdown.

.. dropdown:: What is remote sensing?
   :animate: fade-in
   :chevron: down-up
   :color: info
   :margin: 5

   Remote sensing (RS) can be described as the process of making measurements or observations without direct contact with the object being measured or observed. Thus, while in the geoinformatics context satellites often come to mind, even amateur photography is a form of RS. It usually results in images, but also includes other measurements, such as of temperatures or gravity.

   + **Sensors and platforms**. For remote sensing we normally require a **sensor** (i.e. a camera or scanner), but also something that carries the device. Such platforms can be airplanes or satellites, but also other instruments that allow us to place the sensor so that the area or object of interest is exposed, such as balloons or kites. The choice of platform directly affects what we can observe and how. Airplanes and helicopters are flexible in their operation, and by flying relatively low provide good spatial detail. However, such surveys can be expensive and regular imaging of the same area thus costly. Satellites fly on a fixed **orbit**, and are thus less flexible, but can provide data at regular intervals (think of trains on a track). We distinguish between so-called **polar orbiters**, whereby the satellites continuously circle the Earth at an altitude of some 500- 900km, passing over or near the poles. Normally only a relatively narrow strip of Earth underneath the sensor is observed. Modern satellites can also point the sensor sideways for greater flexibility. The other class of satellites is positioned in **geostationary orbit**. This means that the satellite is always directly above a designated place on the equator, moving with the rotating Earth at an altitude of 36,000 km. At that height the sensor can usually observe an entire hemisphere (the side of the Earth facing it), and provide data at any desired frequency. Many weather and communication satellites fall in this category, while most Earth observation satellites are polar orbiters.

   + **Collecting information**. The data we obtain depend primarily on the sensor type, just like you might take color or black/white photos with your camera. The secret to taking such different photos lies in the **electromagnetic energy** :numref:`the_em_spectrum`, which is what our sensors can detect. The most common source of energy is reflected sunlight, which, as you probably know, contains visible light, but also ultraviolet (UV), infrared (IR), thermal and other energy (Figure 2.1). Which part of this continuous energy band we capture depends on the sensor. Your camera might only capture visible light, while others can “see” UV, IR or thermal energy.

   .. _the_em_spectrum:
   .. figure:: _static/figures/data_for_disaster_risk_managment/the_em_spectrum.jpg
      :alt: The EM spectrum
      :figclass: align

      The EM spectrum

   + **The data**. The data our sensors record typically have the form of a grid, or raster. Rows and columns in that grid are populated by cells. These cells contain the information recorded by the sensor. A sensor can also have several **bands**, meaning that different sections of the electromagnetic spectrum are observed :numref:`grid_structure`. Thus for the area observed we will have an image that contains several bands, and the cell corresponding to a small part on the ground will have one data value for each band. The most important point to understand here is that different materials on the ground reflect energy in a characteristic spectral pattern. For example, vegetation is characterized by high energy in the near infrared (NIR), while for water the energy is very low. In figure 2.2 this would result in high values (digital numbers [DN]) for vegetation and low values for water in the band corresponding to the NIR.

   .. _grid_structure:
   .. figure:: _static/figures/data_for_disaster_risk_managment/grid_structure.png
      :alt: Grid structure of a multi-band image
      :figclass: align

      Grid structure of a multi-band image

   + **Displaying an image**. Once we have our data we can either display them directly on our monitor (if they are already digital), or first scan them. A monitor works with 3 different color channels (blue, green, red), and is able to generate any color (including black and white) with a combination of those 3 colors. Thus we can take an image with only 1 or with several bands and display 1 band at a time, thus as a **pan-chromatic** image :numref:`image_visualizations`. We can also use 3 bands and display them as a so- called **true-color composite** (B), which looks like the scene would look to us from space. However, we can essentially assign any of the image bands to one of the 3 colors. A typical combination, called a **false-color composite**, is shown in C, where the information from the  NIR band is displayed in red. Recall that vegetation leads to high DN values in the NIR, hence the high vegetation signal leads to a

   .. _image_visualizations:
   .. figure:: _static/figures/data_for_disaster_risk_managment/image_visualizations.png
      :alt: A – panchromatic, B- true-color, C and D – false color composites
      :figclass: align

      A – panchromatic, B- true-color, C and D – false color composites
       
   + **Enhancing an image**. Sometimes, for information to be made more visible, we have to enhance the image. One typical form is **stretching**. Our displays are typically able to display 256 brightness levels for each color, corresponding to 8bit. However, very often the image data only have a limited range, say with DNs between 50 and 150, where are not very bright or very dark features on the ground. To achieve a display with a richer contrast we can stretch the data over the entire available range (0-255). The same concept applies to other data types you will work with, for example elevation. The elevation file for our test area ranges between approximately 900 and 1350m. By default they will be stretched over the available display range. However, we can also stretch a small value range, say 950-1000, to highlight more details. Another common enhancing method is **filtering** :numref:`filtering`. This is a so-called neighborhood analysis, often used to smoothen an image or to highlight edges. In the example the average of all cells shown in grey in the input image is calculated and written to a new file, before the filter template moves to the next pixel (hatched box). Many filter types have been developed, which you will also use in the ILWIS exercises (for example shadow and smoothing filters).

    .. _filtering:
    .. figure:: _static/figures/data_for_disaster_risk_managment/filtering.jpg
      :alt: Input and output result of filtering:  In this case, a smoothing filter was applied.
      :figclass: align

      Input and output result of filtering:  In this case, a smoothing filter was applied.

    + **Other factors influencing our data**. RS data come in many forms, often described by **sensor type**, as well as **spatial, temporal** and **spectral resolution**. Sensors recording reflected sunlight or energy emitted by the earth are called **passive sensors**. However, we also have sensors that emit their own energy, which is reflected by the earth, just like you use a flash on your camera. These are **active sensors**, well-known examples being radar (see Figure 2.10) or laser scanning. The **spatial resolution** describes the size of the ground area represented in a single pixel. This largely depends on the distance between the sensor and the object. While aerial photos may have a resolution of a few cm, data from polar orbiters range between about 50 cm and 1 km per cell. Sensors on geostationary satellites, being very far away, record data at resolutions of a few km. The **temporal** resolution describes the possible frequency of repeat observations. For aerial surveys this can be years. Depending on the type of polar orbiter and sensor, their temporal resolution varies between approx. 1 and 44 days, while geostationary sensors record data up to every 15 minutes. The **spectral** resolution describes how narrow a slice of the EM spectrum a sensor band records.

Digital Elevation Models (DEM)
******************************

**Digital Elevation Models (DEM)**  consist of a single band image where the pixel value represents the elevation of that location :numref:`bala_savalan_peak_(Iran)_DEM_srtm`. They are a fundamental and indispensable dataset for many applications because there are many other informations that can be derived from it, especially when it comes to hydrology. In fact, delineation of catchment areas, streams, flood simulations cannot be done without a DEM as input.


.. _bala_savalan_peak_(Iran)_DEM_srtm:
.. figure:: _static/figures/data_for_disaster_risk_managment/bala_savalan_peak_(Iran)_DEM_srtm.png
      :alt: DEM of the Savalan Peak (Iran) based on SRTM data
      :figclass: align

      DEM of the Savalan Peak (Iran) based on SRTM data

DEM are also essential for all sort of landscape analysis for their unique ability to provide an intuitive reading on the main features of an area: where are the mountains, the valleys, the flat areas and so on :numref:`dem_animation`:

.. _dem_animation:
.. figure:: _static/figures/data_for_disaster_risk_managment/dem_animation.gif
      :alt: 3D visualization of the DEM of the Savalan Peak (Iran) based on SRTM data
      :figclass: align

      3D visualization of the DEM of the Savalan Peak (Iran) based on SRTM data

Land Cover Maps
***************

Land Cover maps are a form of thematic data where the map is made of mutually exclusive categories that are defined according to the prevalent land cover.
For example, a land cover map with four categories could include *water*, *green area*, *dry area*, and *urbanized*. Land cover maps are often confused with land use maps, and the two terms are mistakenly used interchangeably. Land cover refers to the actual physical surface of an area—what dominates the landscape :numref:land_cover_enschede.
In contrast, land use maps document how people utilize the land. For instance, green area describes the land cover, but park is a land use category, not a cover type.

.. _land_cover_enschede:
.. figure:: _static/figures/data_for_disaster_risk_managment/land_cover_enschede.png
      :alt: Land cover map of Enschede (The Netherlands) based on Sentinel 2 imagery (2016)
      :figclass: align

      Land cover map of Enschede (The Netherlands) based on Sentinel 2 imagery (2016)

Land cover maps are typically produced by classifying multi-spectral satellite imagery using a range of machine learning and supervised classification techniques. These methods aim to cluster pixels based on radiometric similarity. The accuracy of the classification is then assessed by evaluating whether the assigned categories correctly match the actual land cover.
The more localized a land cover map is, the more accurate and representative the land cover classes tend to be. However, there exists land cover maps at global scale that might be useful even when used for large scale mapping. See for example `Worldwide land cover mapping <Worldwide land cover mapping_>`_

Land Cover Indices
******************

Land Cover Indices are derived from remotely sensed data, primarily multi-spectral satellite imagery, and are expressed on a numerical scale, typically ranging from -1 to 1. Higher values indicate a greater likelihood that the physical characteristic measured by the index is present. These indices are widely used in environmental monitoring, agriculture, urban planning and may also be very useful for disaster risk managing. Indices allow us to analyze vegetation, water bodies, soil, and built-up areas.
A few of these indices are very commonly used:

* Normalized Difference Vegetation Index (NDVI) – Measures vegetation health and density. Defined as:

.. math::

   NDVI = \frac{(NIR - RED)}{(NIR + RED)}

* Normalized Difference Water Index (NDWI) – Indicates the presence of water on the surface (water bodies).

.. math::

   NDWI = \frac{(GREEN - NIR)}{(GREEN + NIR)}

Representing physical characteristics as an indice is a very useful indicator that also allows for a fast and intuitive assessment of complex phenomenon :numref:`indeces_ndvi_ndwi`. There are many indices built on top of remote sensed imagery, you can check this page for a `list of indices <list of indices_>`_

.. _indeces_ndvi_ndwi:
.. figure:: _static/figures/data_for_disaster_risk_managment/indeces_ndvi_ndwi.png
      :alt: NDVI (A) and NDWI (B) indeces for the Sistan Basin, in Iran, as of January 2005.
      :figclass: align

      NDVI (A) and NDWI (B) indeces for the Sistan Basin, in Iran, as of January 2005.


Metereological data
*******************

Aerial and drone photography
****************************

Despite the increasing availability and quality of satellite imagery, mounting a photographic camera on an aerial vehicle is widely used and covers use cases for which satellite imagery is not the best option. In simple terms, if small object recognition is a requirement, then we need imagey that is suitable for small scale mapping.
The biggest difference between satellite and aerial and drone imagery is the spatial resolution that is higher in the latter :numref:`satellite_arerial_drone_imagery`. Commercial satellites offer spacial resolutions, for True colour of up to 3m while with aerial and drone photography we can have imagery with centimetric spatial resolution.

.. _satellite_arerial_drone_imagery:
.. figure:: _static/figures/data_for_disaster_risk_managment/satellite_arerial_drone_imagery.png
      :alt: Imagery documenting Caldas da Rainha, Portugal: (A) Sentinel-2 satellite imagery with a spatial resolution of 10m; (B) a highlighted section of the city captured in aerial photography with a resolution of 10cm; (C) the same highlighted section using drone imagery at 2cm resolution. Notice how the detail increases.
      :figclass: align

      Imagery documenting Caldas da Rainha, Portugal: (A) Sentinel-2 satellite imagery with a spatial resolution of 10m; (B) a highlighted section of the city captured in aerial photography with a resolution of 10cm; (C) the same highlighted section using drone imagery at 2cm resolution. Notice how the detail increases.

Aerial photography is usually comissioned by national agencies to obtain a detailed based map for the whole country or a particular region, while drone imagery, due to the logistic challenge of scaling it up to large areas, is usually applied to cover localized areas like a development plan or a particular part of a city.

Topographic maps
****************

Topographic maps are the result of surveys using traditional optical survey methods like total stations and theodolites, but nowadays, these surveys are typically assisted by GPS measurements and can be complemented with other aerial imagery or even LiDAR and other sensors.
Topographic maps include two big groups of information: man-made structures like roads and buildings and natural features with a great emphasis on altitude measurements that are on the base of terain representations and the deliniation of landscape features like ridges, valleys and water bodies :numref:`topographic_map_example`

.. _topographic_map_example:
.. figure:: _static/figures/data_for_disaster_risk_managment/topographic_map_example.png
      :alt: Detail of a topographic map the Tehachapi Mountains (California, USA). Section of "The National Map" by USGS
      :figclass: align

      Detail of a topographic map the Tehachapi Mountains (California, USA). Section of "The National Map" by USGS

Modern topographic maps are actually a composition of several distinct datasets that were acquired using a myriad of different techniques, however in many countries old paper based topographic maps continue to be a precious source of information.
When a map is made of a a subset of of topographic elements in order to document a specific theme, we call it a 'thematic map'. Common thematic maps include natural features like geology :numref:`geology_map` or man-made elements like communications and cadastral maps (or other delimitations) :numref:`cadastral_map_dorset`.

.. _geology_map:
.. figure:: _static/figures/data_for_disaster_risk_managment/geology_map.png
      :alt: Thematic map of the geology from the peninsula of Peniche (Portugal)
      :figclass: align

      Thematic map of the geology from the peninsula of Peniche (Portugal)

.. _cadastral_map_dorset:
.. figure:: _static/figures/data_for_disaster_risk_managment/cadastral_map_dorset.png
      :alt: Thematic map of the land parcels and roads from Dorset (Tasmania)
      :figclass: align

      Thematic map of the land parcels and roads from Dorset (Tasmania)


LiDAR data
**********

LiDAR or *Light Detection and Ranging* is an active remote sensing system that can be used to generate very high resolution (in other words, detailed) Digital Elevation and Digital Surface Models :numref:`lidar`

.. dropdown:: Difference between DEM and DSM
   :animate: fade-in
   :chevron: down-up
   :color: info
   :margin: 5

   Although DEM (Digital Elevation Models) and DSM (Digital Surface Models) are often mentioned interchangeably, they have slightly different meaning:

   + **DEM** Is a representation of the topography without any other features like constructions or trees. It represents the height of 'bare earth' only :numref:`dem_vs_dsm`.

   + **DSM** In turn, is a representation of the topography that includes features that are on the 'bare soil' like houses and vegetation :numref:`dem_vs_dsm`.

   .. _dem_vs_dsm:
   .. figure:: _static/figures/data_for_disaster_risk_managment/dem_vs_dsm.png
      :alt: Same area as a DEM (A) and DSM (B). Note how the DSM is representing the top of the trees and that reflects in the elevation values.
      :figclass: align

      Same area as a DEM (A) and DSM (B). Note how the DSM is representing the top of the trees and that reflects in the elevation values


.. _lidar:
.. figure:: _static/figures/data_for_disaster_risk_managment/lidar.gif
      :alt: DSM of the Neštich hillfort above Svätý Jur (Slovenia) made from LiDAR data (2016)
      :figclass: align

      DSM of the Neštich hillfort above Svätý Jur (Slovenia) made from LiDAR data (2016)

LiDAR data acquisition is performed using a laser beam, typically mounted on an aircraft. The laser "fires" pulses toward the Earth's surface, with point densities typically ranging from 1 to 100 points per square meter. Higher point densities provide more detailed data but also require more intensive processing.

The collected data forms a point cloud consisting of millions of points, each represented by XYZ coordinates. These coordinates are determined by measuring the time it takes for the laser beam to reach an object and reflect back to the sensor.

One particularly interesting application of high-density point clouds is their ability to penetrate vegetation and capture multiple layers of information. This allows for the identification of different levels, such as bare soil, intermediate vegetation, and the top of the tree canopy :numref:`lidar_flying`.

   .. _lidar_flying:
   .. figure:: _static/figures/data_for_disaster_risk_managment/lidar_flying.gif
      :alt: Animation illustrating the level of detail collected with a LiDAR sensor mounted on an airplane.
      :figclass: align

      Animation illustrating the level of detail collected with a LiDAR sensor mounted on an airplane

Crowd source data
*****************

Census and Statistica data
**************************

Sources of data, acess and dissemination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data sharing and dissemination (1-1.5 hour exercise)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data quality (granularity, fitness for purpose)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data sovereignty (control , licensing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
