[Ocean and Coastal Management 233 (2023) 106466](https://doi.org/10.1016/j.ocecoaman.2022.106466)


Contents lists available at ScienceDirect

# Ocean and Coastal Management

[journal homepage: www.elsevier.com/locate/ocecoaman](https://www.elsevier.com/locate/ocecoaman)


#### Review

## Using artificial intelligence to support marine macrolitter research: A content analysis and an online database

### Dimitris V. Politikos [a][,] [*], Argyro Adamopoulou [b], George Petasis [c], Francois Galgani [d ]

a Institute of Marine Biological Resources and Inland Waters, Hellenic Centre for Marine Research, 16452, Argyroupoli, Greece
b Institute of Oceanography, Hellenic Centre for Marine Research, Anavyssos, Greece
cd Institute of Informatics and Telecommunications, National Centre for Scientific Research Institut Français de Recherche pour l’ Exploitation de la Mer (IFREMER), Brest, France  “Demokritos”, 60228, Agia Paraskevi, Greece


A R T I C L E I N F O

_Keywords:_
Beached/dune

Floating
Seafloor
Deep learning
Machine learning

**1. Introduction**


A B S T R A C T

Marine scientists use a variety of collection and monitoring methods to survey macrolitter in aquatic environ­
ments, aiming to assess the level of pollution and design mitigation actions. However, the large volume of
collected data often makes the visual recognition and identification of macrolitter items a time-consuming and
labor-intensive task, indicating the need for automated and low-cost solutions. In addition, modelling approaches
are needed to identify which environmental and anthropogenic factors shape the variability of observed litter
concentrations. Artificial intelligence (AI) has emerged over the last years as a promising tool to address these
issues. This study provides a literature review of published research that uses AI to process macrolitter datasets
derived from imagery and tabular data. The focus is on diverse topics (litter domain, dataset source, sampling
system, data type, task to be resolved, region, proposed methodologies, usability) with the aim of identifying the
versatile contribution of AI on this theme and providing a reference resource for marine litter scientists. To do so,
we release an online database (available here), in which the user can seek publications based on several cate­
gories and tags. Current limitations, challenges and potential future directions are also discussed.


Litter pollution is a growing problem, posing a pervasive threat to
marine and freshwater ecosystems around the globe (Eriksen et al., 2014;
Ostle et al., 2019). Marine litter has been documented in all water bodies
and coastal lands, from lakes (Driedger et al., 2015; Zbyszewski et al.,
2014) and the surface of the oceans (Eriksen et al., 2014), to rivers (Hel­
inski et al., 2021), seafloor (Galgani et al., 2000; Ioakeimidis et al., 2014)
beaches (Haseler et al., 2018) and dunes (Andriolo and Gonçalves, 2022).
It can cause physical harm or kill marine fauna through ingestion and
entanglement with more than 1400 different species found to be affected
(Galgani et al., 2019). Animal species like fish, birds, and invertebrates are
especially affected by micro- and meso-litter[1 ] made mainly of plastics
(NOAA, 2014). Additionally, meso- and macro-litter[1 ]can degrade coastal
habitats and the quality of life in coastal communities, while micro- and
nano-litter[1 ]can pass across the seafood chain and threaten human health


(Clark et al., 2022; UNEP/MAP and United, 2016).
Surveys are conducted worldwide to assess the type, size, abundance,
and spatial distribution of collected marine litter items with the aim of
assessing the level of pollution and designing management actions that
will promote litter removal and recycling (Canals et al., 2021; Forrest et al.,
2019; Kershaw et al., 2019; Madricardo et al., 2019; Pham et al., 2014).
Concurrently, hydrodynamic models coupled with particle tracking
models have attempted to improve our understanding of the sources,
transport, and pathways of marine litter at the open sea and coastal waters
(Hardesty et al., 2017; NOAA 2016; van Sebille et al., 2020).
Nowadays, scientists have at their disposal a variety of collection and
monitoring methods to monitor and assess marine litter in aquatic
ecosystems (Maximenko et al., 2019; Salgado-Hernanz et al., 2021).
In-situ visual census surveys (e.g., beachcombing) is the most techni­
cally simplistic way to directly collect data about meso/macro-litter
(GESAMP, 2019; Thiel et al., 2003) since they are visible to the naked



 - Corresponding author.
_[E-mail address: dimpolit@hcmr.gr (D.V. Politikos).](mailto:dimpolit@hcmr.gr)_
1 Macro(>25 mm)- and meso(5–25 mm)- marine litter are objects that can be monitored by visual census. Litter also enters the environment as very small particles,
the so-called microlitter (300 μm - 5 mm) or nanolitter (<300 μm). These are usually derived from fragmentation of larger litter items through different processes
such as photodegradation, physical degradation and hydrolysis (Fotopoulou and Karapanagioti, 2017).

[https://doi.org/10.1016/j.ocecoaman.2022.106466](https://doi.org/10.1016/j.ocecoaman.2022.106466)
Received 2 August 2022; Received in revised form 2 December 2022; Accepted 16 December 2022

Available online 29 December 2022
0964-5691/© 2022 Elsevier Ltd. All rights reserved.


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


eye. Other data acquisition systems include bottom trawlers to collect
seafloor macrolitter (Canals et al., 2021), manta or neuston nets to
collect floating microlitter at the open sea (Mor´et-Ferguson et al., 2010), and optical devicesAdamopoulou et al., 2021[2 ]to identify macrolitter ;
items on beaches (Escobar-Sanchez et al., 2021´ ; Hengstmann and
Fischer, 2020; Lo et al., 2020; Taddia et al., 2021), dunes (Andriolo
et al., 2020, 2021a) and seafloor (Fakiris et al., 2022; Madricardo et al.,
2019). Accordingly, optical devices and satellite sensors are used to
monitor floating macrolitter (Garcia-Garin et al., 2020a,b; Mukonza and
Chiang, 2022; Topouzelis et al., 2021), while echosounder systems have
also been used for monitoring underwater litter (Broere et al., 2021).
However, the recognition and assessment of macrolitter pollution are
confronted with the need for processing big volume of data to charac­
terize litter items, a process that is time-consuming, subjective, and
labor-intensive. Standard methods of macrolitter assessment are based

on manual image screening and marking processes performed by trained
scientists (Andriolo et al., 2021b; Andriolo and Gonçalves, 2022; Gar­
cia-Garin et al., 2021; Merlino et al., 2021; Papachristopoulou et al.,
2020). Additionally, aerial- and satellite-based remote sensing meth­
odologies have also been proposed for detecting beached and floating
macrolitter (Andriolo et al., 2021a; Cocking et al., 2022; Kataoka et al.,
2012; Kataoka and Nihei, 2020; Themistocleous et al., 2020; Wang et al.,
2015). Developing methods that will promote automated and rapid so­
lutions for macrolitter identification has been recognized as a worthy
goal (Canals et al., 2021; Garcia-Garin et al., 2021). Additionally,
identifying key environmental and anthropogenic factors driving ma­
rine macrolitter accumulation is also a valuable task that needs efficient
modelling approaches (Kaandorp et al., 2022).
Artificial Intelligence (AI) is a branch of computer science and en­
gineering that attempts to create machines that behave as intelligent as
humans (Goodfellow et al., 2015). The two subfields of AI, machine
learning (ML) and deep learning (DL), have revolutionized a wide range
of real-world applications by automating processes related to tabular
data, images, video, speech, audio, and text (Alpaydın, 2014; Deng and
Liu, 2018; Gao et al., 2020; LeCun et al., 2015).
In recent years, AІ has gained attention in marine litter research by
providing automatic visual recognition and identification both of macrolitter/plastics (Gnann et al., 2022; Karakus¸, 2022; Mukonza and Chiang,
2022; Salgado-Hernanz et al., 2021; Topouzelis et al., 2021) and
micro-litter/plastics (Lin et al., 2022; Mukonza and Chiang, 2022). In this
paper, we provide a literature review of published research that uses AI to
process marine litter datasets, with a special focus on macrolitter imagery
and tabular data. Collected papers were tagged and analyzed under
diverse aspects in order to identify the versatile contribution of AI on this
theme, as well highlight current limitations, challenges and future di­
rections. Finally, the surveyed papers were organized into an online
database from which researchers could seek publications based on
several categories and tags. The database is operational; new publications
will be uploaded regularly, providing a convenient way for non-computer
scientists to keep track of the latest AI-marine litter advancements.
Compared to the AI-macrolitter reviews, we extended the literature
search to all macrolitter domains (beached, dune, floating, seafloor),
multiple observing/sampling systems, and different dataset sources (insitu, publicly available, experimental, synthetic). We also focused on
technical aspects of the adopted AI methodologies (architectures, pre­
dictive accuracy, task to be resolved, and usability).

**2. Literature search and selection criteria**

We surveyed the literature for AI applications in marine macrolitter
research, using widely used databases for archiving scientific articles,

2 Drones, Autonomous Underwater Vehicles (AUVs), Remotely Operated
Vehicles (ROVs), Unmanned Aerial Systems (UAS), vessel-mounted or landbased cameras, sonars, and satellites.


**Table 1**

Keywords used as search criteria for collecting the literature.

AI Random Forest

Marine litter AND Machine Learning SVM
Marine debris Deep Learning Classification
Marine (macro)plastics CNN Detection

Neural networks

namely Wiley Online Library, IEEE, Elsevier/ScienceDirect, Scopus, and
Web of Science. The keywords used as search criteria are shown in Table 1.
After reviewing the content of the resulting articles to ensure their rele­
vance to our research topic, we ended up with 80 articles, covering the
period from 2004 to October 2022. We excluded sources that did not have
a digital object identifier (DOI), did not implement an AI workflow (see
Section 3
), did not include clearly defined data sources, and non-English
papers. The list of collected articles can be found in Table 2.

**3. General AI workflow applied in marine macrolitter research**

A generic AI workflow, as applied to a marine macrolitter dataset for
the various data types and tasks, is shown in Fig. 1. The litter dataset is

or
first retrieved; this data can be images, orthomosaics/orthophotos,[3 ]
tabular.[4 ] Second, the AI task to be resolved is defined. The main tasks
found in the collected papers are classification, object detection,
instance segmentation, semantic segmentation, quantification (through
segmentation), and regression. More details about the scope of these AI
tasks can be found in the Appendix; a visual overview of the tasks is also
shown in Fig. 2. Third, a preprocessing of the dataset is essential to
prepare the data so that AI algorithms can parse it. Common works
during the data preprocessing step include image labeling[5]; bounding
box annotation[6]; cleaning of tabular data[7]; feature extraction from im­
ages[8]; extraction of orthophotos from orthomosaic images; segmenta­
tion of orthophotos into tiles; and the enhancement of image quality.[9 ]

Fourth, one or more (for comparison reasons) algorithms are selected to
resolve the defined task. The architectures found in the collected papers
were convolutional neural network (CNN), object detection architecture
(OD), feed forward neural network (FFNN), machine learning algorithm
(MLA), encoder-decoder architecture (EDA), instance segmentation

3 Orthophotos are image data composed of dozens, hundreds, or thousands of
smaller overlapping images, typically captured with a drone or UAV. These
images are “stitched together” with specialized photogrammetry software,
resulting in an orthomosaic image.

4 Tabular data includes numeric and categorical values structured into rows,
each of which contains column information of interest. Tabular data include

measurements of litter abundance/density and environmental/anthropogenic
variables such as waves, currents, wind speed, tides, beach exposure, marine
traffic density, etc. (Kaandorp et al., 2022; Martin et al., 2021).

5 The process of annotating the type of litter in an image, e.g., bottle. An­
notated images are used for training and evaluating classification and detection
tasks.

6 The process of annotating the type of litter in an image, e.g., bottle. An­
notated images are used for training and evaluating classification and detection
tasks.

7 Data cleaning includes several potential tasks such as removal of duplicate
observations, correct errors and missing data, handle outliers.

8 Features are extracted from images with several methods such as waveform
data (Ge et al., 2016), RGB and NIR bands (Cortesi et al., 2022), spectral indices
(Biermann et al., 2020; Jamali and Mahdianpari, 2021; Mikeli et al., 2022;
Lavender, 2022; Sannigraphi et al., 2022; Sasaki et al., 2022) and other feature
descriptors such as histogram of gradient, grey level co-occurrence matrix
(GLCM) Gabor, histogram, normalization of bands, point sampling (Ramdani
et al., 2022; Savastano et al., 2021; Sasaki et al., 2022; Taggio et al., 2022).

9 Enhancement of image quality includes noise removal, and atmospheric,
radiometric and sun glint corrections (Aleem et al., 2022; Basu et al., 2021;
Booth et al., 2022; Lavender, 2022; Sannigraphi et al., 2022; Savastano et al.,
2021).


2


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Table 2**
List of surveyed scientific articles (n = 80) under the scope of this review. Details about the included content categories and tags can be found in Section 4.

References Sampling system Dataset type Litter domain Usability Dataset source Task Architecture

Acuna-Ruz et al. (2018) ˜ Satellite (Sentinel-2 Image Beached/Dune Litter In-situ Classification, MLA
or WorldView-3) assessment Quantification

Aleem et al. (2022) Sonar Sonar image Floating, PPA Public Classification, Detection OD
Seafloor

Andriolo et al. (2022) UAV/UAS Orthomosaic/ Floating, PPA In-situ Classification MLA
Orthophoto, Image Beached/Dune

Armitage et al. (2022) Camera Image Floating PPA Experimental Classification, Detection OD
Bajaj et al. (2021) AUV/ROV Image Seafloor PPA Public Detection OD
Bak et al. (2019) UAV/UAS Orthomosaic/ Beached/Dune PPA In-situ Semantic segmentation Sem-Seg
Orthophoto

Balas et al. (2004) Visual census Image Beached/Dune PPA In-situ Regression FFNN
Balas et al. (2006) Visual census Tabular Beached/Dune PPA In-situ Regression FFNN
Basu et al. (2021) Satellite (Sentinel-2 Image Floating PPA Experimental Classification, Semantic MLA,
or WorldView-3) segmentation Clustering
Biermann et al. (2020) Satellite (Sentinel-2 Image Floating PPA In-situ Classification MLA
or WorldView-3)

Booth et al. (2022) Satellite (Sentinel-2 Image Floating Litter Experimental Classification, Semantic MLA, Sem-Seg
or WorldView-3) assessment segmentation

Chang et al. (2020) Camera Image Beached/Dune PPA In-situ Classification CNN
Chin et al. (2022) Cordova et al. (2022) ´ Camera Image Image Seafloor Floating, PPA PPA Public Public Classification, Detection Detection OD OD
Beached/Dune

Cortesi et al. (2022) Camera Image Floating, PPA In-situ Classification, Semantic MLA
Beached/Dune segmentation

Cortesi et al. (2022) UAV/UAS Image Floating PPA In-situ Classification, Semantic MLA
segmentation

de Vries et al. (2021) UAV/UAS, Camera Image Floating Litter In-situ Classification, OD
assessment Quantification

Deng et al. (2021) AUV/ROV Image Seafloor PPA Public Classification, Detection OD
Duarte et al. (2020) UAV/UAS Orthomosaic/ Beached/Dune PPA In-situ Classification CNN
Orthophoto

Fallati et al. (2019) UAV/UAS Orthomosaic/ Beached/Dune PPA In-situ Classification, Detection CNN
Orthophoto

Fossum (2022) AUV/ROV Image Seafloor PPA In-situ Classification, Detection OD
Franceschini et al. Bottom trawlers Tabular Seafloor Exploratory In-situ Regression FFNN
(2019)

Freitas et al. (2021) UAV/UAS Image Beached/Dune PPA Experimental Classification, Detection MLA
Fulton et al. (2018) AUV/ROV Image Seafloor PPA Public Classification, Detection OD
Garcia-Garin et al. UAV/UAS Image Floating Litter Experimental Classification CNN
(2021) assessment

Ge et al. (2016) Camera Image Beached/Dune PPA Experimental Classification, Semantic MLA
segmentation

Gomez et al. (2022) ´ Satellite (Sentinel-2 Image Floating PPA In-situ Detection OD
or WorldView-3)

Gonçalves et al. UAV/UAS Orthomosaic/ Beached/Dune Litter In-situ Detection, Quantification MLA
(2020a) Orthophoto assessment

Gonçalves et al. UAV/UAS Orthomosaic/ Beached/Dune Litter In-situ Detection, Quantification MLA, CNN
(2020b) Orthophoto assessment

Gonçalves et al. UAV/UAS Orthomosaic/ Beached/Dune Litter In-situ Classification, Semantic MLA
(2020c) Orthophoto assessment segmentation

Hidaka et al. (2022) Camera Image Beached/Dune PPA In-situ Classification, Detection, Sem-Seg
Semantic segmentation

Hong et al. (2020a) AUV/ROV Image Floating, PPA Public Classification EDA
Seafloor

Hong et al. (2020b) AUV/ROV Image Seafloor PPA Public Classification, Detection, OD, Ins-Seg
Instance segmentation

Jakovljevic et al. UAV/UAS Orthomosaic/ Floating PPA Experimental Classification, Semantic Sem-Seg
(2020) Orthophoto segmentation

Jamali and Satellite (Sentinel-2 Image Floating PPA Experimental Classification, Semantic MLA
Mahdianpari (2021) or WorldView-3) segmentation

Kaandorp et al. (2022) Visual census Tabular Beached/Dune Exploratory In-situ Regression MLA
Kako et al. (2020) UAV/UAS Image Beached/Dune Litter Experimental Semantic segmentation, FFNN
assessment Quantification

Kankane and Kang Camera Image Beached/Dune PPA In-situ Semantic segmentation OD
(2021)

Kikaki et al. (2022) Satellite (Sentinel-2 Image Floating PPA In-situ Classification, Semantic MLA, Sem-Seg
or WorldView-3) segmentation

Kylili et al. (2019) Camera Image Floating PPA Public Classification CNN
Kylili et al. (2020) Image Floating PPA Public Classification CNN
Kylili et al. (2021) Image Beached/Dune PPA Public Classification, Detection OD
Lavender (2022) Satellite (Sentinel-2 Image Floating PPA In-situ Classification, Semantic MLA, FFNN
or WorldView-3) segmentation

Lin et al. (2021) Camera Image Floating PPA Synthetic Detection OD
Maharjan et al. (2022) UAV/UAS Image Floating PPA In-situ Classification, Detection OD

(continued on next page)

3


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Table 2 (continued** )

References Sampling system Dataset type Litter domain Usability Dataset source Task Architecture

Majchrowska et al. Image Floating, PPA Public Classification, Detection OD
(2022) Seafloor

Mallick et al. (2021) Sonar image PPA Public Classification CNN
Martin et al. (2021) Image Seafloor PPA Public Classification CNN
Martin et al. (2018) UAV/UAS Image Beached/Dune PPA In-situ Classification MLA
Martin et al. (2021) UAV/UAS Image, Tabular Beached/Dune PPA, In-situ Detection, Regression OD
Exploratory

Mifdal et al. (2021) Satellite (Sentinel-2 Image Floating PPA In-situ Semantic segmentation CNN, Sem-Seg,
or WorldView-3) MLA
Mikeli et al. (2022) Satellite (Sentinel-2 Image Floating PPA In-situ Classification, Semantic MLA, Sem-Seg
or WorldView-3) segmentation

Moorton et al. (2022) Image Seafloor PPA Synthetic Classification CNN
Moshtaghi and Knaeps UAV/UAS Image Floating PPA Experimental Detection OD
(2021)

Musi´c et al. (2020) Image Floating, PPA Synthetic Classification, Detection OD
Seafloor

Nazerdeylami et al. Camera Image Beached/Dune PPA In-situ, Public Classification, Detection OD
(2021)

Panwar et al. (2020) Image Floating PPA Public Classification, Detection OD
Papakonstantinou et al. UAV/UAS Image Beached/Dune Litter In-situ Classification, CNN
(2021) assessment Quantification

Pinto et al. (2021) UAV/UAS Orthomosaic/ Beached/Dune Litter In-situ Classification FFNN
Orthophoto assessment

Politikos et al. (2021) AUV/ROV Image Seafloor PPA In-situ Classification, Detection, OD
Instance segmentation

Priyadarshini et al. Tabular Beached/Dune PPA Public Classification MLA
(2022)

Ramdani et al. (2022) UAV/UAS Image Floating PPA In-situ Classification, Semantic MLA, FFNN
segmentation

Sanchez-Ferrer et al. ´ Image Floating, PPA Public Classification, Semantic OD
(2022) Seafloor segmentation

Sannigraphi et al. Satellite (Sentinel-2 Image Floating PPA In-situ, Classification, Semantic MLA
(2022) or WorldView-3) Experimental segmentation

Sasaki et al. (2022) Satellite (Sentinel-2 Image Beached/Dune Litter In-situ Classification, Semantic MLA, FFNN
or WorldView-3) assessment segmentation

Savastano et al. (2021) Satellite (Sentinel-2 Image Floating PPA Experimental Classification, Semantic MLA
or WorldView-3) segmentation

Schulz and Matthies Visual census Tabular Beached/Dune Exploratory In-situ Regression FFNN
(2014)

Song et al. (2021) Camera Image Beached/Dune PPA In-situ Classification, Detection, OD
Quantification

Taggio et al. (2022) Satellite (Sentinel-2 Image Floating PPA Experimental Classification, Semantic MLA,
or WorldView-3) segmentation Clustering
Takaya et al. (2022) UAV/UAS Image Beached/Dune PPA In-situ Classification, Detection OD
Tata et al. (2021) Camera Image Floating, PPA Public Detection OD
Seafloor

Teng et al. (2022) Image Beached/Dune PPA Public Classification, Detection OD
Tharani et al. (2020) Camera Image Floating PPA Public Detection OD
Valdenegro-Toro Sonar Sonar image Floating PPA Public Classification, Detection OD
(2016)

van Lieshout et al. Camera Image Floating Litter In-situ Classification, Detection, OD
(2020) assessment Quantification

Veerasingam et al. Camera Image Beached/Dune PPA In-situ Detection OD
(2022)

Watanabe et al. (2019) UAV/UAS Image Floating, PPA In-situ Detection OD
Beached/Dune

Wolf et al. (2020) UAV/UAS Image Floating, PPA In-situ Classification, MLA, CNN
Beached/Dune Quantification

Xue et al. (2021a) Image Seafloor PPA Public Classification CNN
Xue et al. (2021a) Image Seafloor PPA Public Classification, Detection OD


architecture (Inst-Seg), semantic segmentation architecture (Seg-Sem),
and clustering. More details about the AI architectures can be found in
the Appendix. Fifth, the dataset is split into the train and validation
subsets, which are being used to train the AI algorithm(s) through
hyperparameter tuning[10]. In the sixth step, an unknown to the training

10 Hyperparameters are parameters that control the structure of an algorithm
(e.g., number of hidden layers or nodes) and how an algorithm gains experience
(e.g., learning rate) during the training phase. They are set before training and
fine-tuned with the aim of maximizing the learning process of the network.
Fine-tuning is a critical step in any AI pipeline that results in a trained and
validated algorithm that can then be used to make predictions.


process dataset, called a test set (also created during the dataset split), is
used to evaluate the predictive performance of the trained algorithm
using the task-based evaluation metrics (Fig. 2). More details about the
evaluation metrics can be found in the Appendix.

**4. Content analysis**

A content analysis was conducted to review the collected literature.
Content analysis explores the existence and frequency of words, con­
cepts, or themes in a text that are related to a question of interest (Elo
and Kyng¨as, 2008; Krippendorff, 1980). Content analysis is more than a
counting process; it aims to identify intentions, states, beliefs, trends,
patterns, biases, and limitations in order to increase our knowledge and


4


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Fig. 1. Generic view of AI workflow, as applied to a marine litter dataset for common data types and tasks.**

understanding of specific phenomena (Downe-Wamboldt, 1992; Krip­ authors created synthetic images for their analysis, by superimposing
pendorff, 1980). To implement a content analysis, text is coded into marine natural background images on litter items (e.g., Lin et al., 2021;
content categories and topics so that the researcher can look for simi­ Moorton et al., 2022). These different sources of datasets were classified
larities, differences, and relationships among them. into the “Dataset source” category through the four tags: Public, In-situ,
To compile the content information of the collected publications, an _Experimental and Synthetic._
excel sheet was designed with the list of papers on the rows, and the The collection of litter data can take place with various monitoring
following content categories on the columns: “Litter domain”, “Dataset systems, depending on the type of litter. Underwater and seafloor litter
source”, “Sampling system”, “Data type”, “Task”, “Region”, “Architec­ imagery are being collected mainly with UAV (Underwater Autonomous
ture”, and “Usability” (Table 3). Within each content category, specific _Vehicles) and ROV (Remotely Operated Vehicles) and Sonar, and seafloor_
tags were defined to further associate related content in the documents. litter items with bottom trawlers. Floating and beached litter images are
Marine macrolitter items are mainly deposited on three landscapes: being collected through in-situ visual census, _UAS (Unmanned Aerial_
beaches/dunes, on the sea surface, and at the sea bottom. The “Litter _Systems), UAV (Unmanned Autonomous Vehicles), Satellite (Sentinel-2 or_
domain” category was, therefore, represented by three tags, namely, _WorldView-3), and_ _Camera. These systems were used as tags in the_
_Beached/Dune, Floating, and Seafloor._ “Sampling system” category, as UAV/UAS, AUV/ROV, Satellite (SentinelThe marine litter data used in the surveyed documents were provided _2 or WorldView-3), Sonar, Visual census, Camera,_ and _Bottom trawlers_
from four main sources: publicly available datasets, in-situ surveys, (Table 3).
experimental data, and synthetic data. Several open-source datasets Four tags were used to classify the type of marine macrolitter data
with (marine)litter images have been created with the aim of being used in the collected papers through the “Data type” category, corre­
processed with ML/DL techniques; the most known public datasets in sponding to _Image, Orthomosaic/Orthophoto, Sonar image,_ and _Tabular_
the literature are: Trash-ICRA19 (Fulton et al., 2019), TrashCan 1.0 (Table 3).
(2021Hong et al., 2020), TACO (Proença and Sim), PlastOPol (Coes, 2020˜ordova et al., 2022´ ), Forward-Looking sonar ma­), DeepPlastic (Tata, into the The main tasks identified in the collected publications were grouped “Task” category through eight tags, that is: _Classification,_
rine debris dataset,[11 ]Deep-Sea Debris Database (JAMSTEC, 2018), and _Detection, Instance Segmentation, Semantic Segmentation, Quantification,_
the Marine Debris Tracker.[12 ]Additionally, web-scraping of litter images and Regression (Table 3; Appendix).
has been used as an alternative data source (e.g., Musi´c et al., 2020; The sites of the studies that used in-situ litter surveys were assigned
Kylili et al., 2019). All these datasets include a wide variety of both into “Region” category in coordinates (Longitude, Latitude) to depict their
landscape and marine litter images, generated from indoor and outdoor geographic distribution (Table 3).
scenes, with multiple litter categories of different size and material (e.g., Seven tags were chosen to group the different ML/DL architectures
glass, paper, cardboard, plastic, metal, tiles, cups, cans, nets, wood). adopted in the collected papers through the “Architecture” category,
Contrary, in-situ litter surveys are conducted by marine research in­ that is: CNN, OD, FFNN, MLA, EDA, Ins-Seg and Seg-Sem and Clustering
stitutes in specific regions, following protocols, sampling systems and (Table 3; Appendix).
methodologies that meet their scientific goals. In some studies, marine Finally, we classified the usability of the reviewed studies in the
litter was artificially deposited by researchers on the sea surface (e.g., “Usability” category, based on three tags: PPA (Predictive Performance
Armitage et al., 2022; Booth et al., 2022; Jamali and Mahdianpari, 2021; of the Architecture(s) for papers that primarily focused on technical
Moshtaghi and Knaeps, 2021; Savastano et al., 2021; Taggio et al., 2022; aspects by evaluating how good were the adopted ML/DL algorithms to
Topouzelis et al., 2019) or beach (Kako et al., 2020) and experiments automatically recognize macrolitter items on imagery; Litter assessment
were designed to detect marine macrolitter with AI methods, while some for studies that went beyond the predictive performance of the algo­

rithms, attempting to serve as tools that will automatically assess the
abundance (items per surface of cube area) or density (kg per surface

11 area) of litter from _in-situ_ surveys; and _Exploratory_ for studies that

.
[https://github.com/mvaldenegro/marine-debris-fls-datasets/releases/](https://github.com/mvaldenegro/marine-debris-fls-datasets/releases/)
12 [https://www.debristracker.org/.](https://www.debristracker.org/) explored the influence of environmental and anthropogenic variables on

5


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Table 3**

Content categories and tags used to explore the use of AI on marine macrolitter
datasets. Architectures: Convolutional Neural Network (CNN), Object Detection
architecture (OD), Feed Forward Neural Network (FFNN), Machine Learning
Algorithms (MLA), Encoder-Decoder architecture (EDA), Instance Segmentation
architecture (Inst-Seg) and Semantic Segmentation architecture (Seg-Sem) and
Clustering. More details about the AI architectures can be found in the Appendix.

Content Tags

category

Litter domain Beached/Dune, Floating, Seafloor
Dataset source Public, In-situ, Experimental, Synthetic
Sampling (AUV) Autonomous Underwater Vehicles, ROV (Remotely
system Operated Vehicles), Visual census, UAS (Unmanned Aerial
Systems), UAV (Unmanned Autonomous Vehicles), Sonar,
Sentinel-2 satellite, Camera
Data type Image, Orthomosaic/Orthophoto, Sonar image, Tabular
Task Classification, Detection, Instance Segmentation, Semantic
Segmentation, Quantification, Regression
Region (Longitude, Latitude)
Architecture CNN, OD, FFNN, MLA, EDA, Ins-Seg, Seg-Sem, Clustering
Usability Predictive Performance of the Architecture(s) (PPA), Litter
assessment, Exploratory


**Fig. 2. Examples of tasks, as applied to marine macrolitter imagery and tabular**
data, with illustrations of the corresponding techniques and evaluation metrics.
More details about the tasks and the evaluation metrics can be found in

the Appendix.

the distribution and abundance of collected macrolitter (Table 3).
We note that multiple tags were possible within one paper for the
categories “Litter domain”, “Task”, “Architecture” and “Region”.

**5. Online database**

An online database with the collected papers was created. In
particular, the database includes an interactive table from which the
user can seek papers based on the adopted content categories and tags,
as well as auxiliary bibliometric information such as title, year, author,
and DOI link. The database is operational and new publications will be
uploaded regularly, aiming to become a resource for marine scientists
that want to follow the state-of-the-art progress of AI on the theme. The
[database was built with the Streamlit Python library (https://streamlit.](https://streamlit.io/)
[io/), and it’s available here.](https://streamlit.io/)

**6. Analysis results**

From 2004 to October 2022, the rate of yearly publications referring
to AI and marine litter did not follow a linear pattern (Fig. 3). Before
2016, one published article per year explored the theme. Since 2016,
there is an increased interest in the topic, with more than 15 papers per


**Fig. 3. Number of publications per year that implemented AI techniques on**
marine macrolitter datasets.

year in 2020 and 2021.26 publications were reported until October
2022 (the end of the current review), indicating a potential growth in
the annual rate of publications in the years to come. The observed trend
may be attributed to two main factors. First, the development of highly
effective AI algorithms, in combination with the rise of computing
power[13 ] and the release of open-source codes in distributed control
systems (e.g., GitHub), allowed thousands of practitioners to apply AI in
all real-world application domains. Second, the increasing interest in
collecting and analyzing marine litter data in all water bodies in recent
years (Andriolo et al., 2020; Canals et al., 2021; Escobar-S´anchez et al.,
2021; Garcia-Garin et al., 2020a,b; Gauci et al., 2019; Merlino et al.,

2020
) favored the applicability of AI in this scientific field.
The geographical distribution of AI studies that used in-situ marine
macrolitter datasets (without including satellite data) is shown in Fig. 4.
Although marine litter has a worldwide presence, the spatial coverage of
these studies was rather limited. The most studied continents were
Europe and Asia, targeting mainly floating and beached litter, whereas
no in-situ studies have been reported on the African and Australian

13 The rise of graphics processing unit (GPU) technology accelerated the high
demands of computational processing in AI algorithms.


6


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


continents. One study was conducted in North America, referring to
floating litter. Finally, in-situ seafloor litter was studied in two publi­
cations, found in the eastern Mediterranean Sea and northern Europe.
The full list of publications per country can be found in the online
database.

Accordingly, nine studies combined satellite image data and AI
methods to detect beached/dune (two studies) and floating (seven
studies) litter (Fig. 5). These studies demonstrated greater spatial
coverage compared to non-satellite data, with sampling sites located on
all seven continents. This can be attributed mainly to the free access to
image data provided by remote sensing satellites such as WorldView-2
[or 3 and Sentinel-2 (https://earth.esa.int/eogateway;](https://earth.esa.int/eogateway) Kristollari and
Karathanassi, 2020).
The number of publications per content category is shown in Fig. 6.
Most studies focused on floating (42.2%) and beached/dune (37.8%)
litter, and less on seafloor litter (20.0%). In-situ datasets were found in
51.2% of cases, followed by public datasets (29.3%), experimental data
(15.9%) and synthetic data (3.7%). A variety of sampling systems were
used to collect litter data, with UAV/UAS (34.3%), Camera (22.4%) and
Satellite (Sentinel-2 or WorldView-3) (20.9%) being the most frequent.
Regarding the dataset type, images (78.0%) were mostly used, followed
by orthomosaics/orthophotos (11%), tabular data (7.3%), and sonar
images (3.7%). Most papers had as a task the classification (44.4%) and
detection (26.3%) of litter objects, and then semantic segmentation
(16.5%), quantification (6.8%), regression (4.5%), and instance seg­
mentation (1.5%). OD (35.5%) and MLA (28.0%) were the most
frequent architectures used by scientists. Additionally, CNNs were used
in 15.1% of cases, whereas FFNN (9.7%), Sem-Seg (7.5%), Clustering
(2.2%), EDA (1.1%) and Ins-Seg (1.1%) were the less adopted archi­
tectures. Finally, the vast majority of collected papers restricted their
analysis to the evaluation of the involved AI architectures (80.2%), with
less providing an automatic way of litter assessment (14.8%) or an
exploratory analysis (4.9%). Interested readers can seek publications
based on content category on the online database.
The frequency distribution of publications at the intersection of the
content categories “Litter domain” and “Dataset source” is shown in
Fig. 7. Studies that used beached/dune litter were mostly based on insitu datasets (n = 28), with only n = 5 studies using public datasets.
In contrast, the processing of seafloor litter images was done mostly with
public datasets (n = 13), with only n = 2 case using in-situ regional
surveys. For floating litter, studies were rather balanced among public
(n = 11), in-situ (n = 17) and experimental (n = 10) data. Readers can
query publications of interest on the online database, using the filters in
the columns “Litter domain” and “Dataset source”.

The frequency distribution of publications at the intersection of
content categories “Litter domain” and “Task” is shown in Fig. 8. For
beached/dune litter, classification (n = 21) and detection (n = 14) were
the most frequent tasks, followed by semantic segmentation (n = 8),
quantification (n = 7), and regression (n = 5) tasks. Similarly, classifi­
cation (n = 30) and semantic segmentation (n = 15) were mainly con­
ducted for floating litter and less for other tasks. Seafloor litter was
mostly studied for classification (n = 15) and detection (n = 12), with
two studies (n = 2) focusing on segmentation tasks. Readers can query
publications of interest in the online database using the filters in the
columns “Litter domain” and “Task”.

**7. Discussion**

In this study, we collected and analyzed scientific articles at the
intersection of AI and marine macrolitter research. Review results

showed that a variety of AI algorithms have been implemented and
evaluated on macrolitter imagery and tabular data, attaining significant
progress on the automatic classification, object detection, and segmen­
tation of macrolitter objects, as well as exploring which environmental
and anthropogenic variables can affect the observed litter abundance/
density on the beach and seafloor. Moreover, AI has made its first steps


towards supporting automated litter assessment from in-situ surveys by
estimating the mass (kg/m[2]) (Acuna-Ruz et al., 2018˜ ) and abundance of
beached litter (at scales of items/km[2 ] or items/m[2 ] or items/m[3]) (de
Vries et al., 2021; Garcia-Garin et al., 2021; Gonçalves et al., 2020a,b,c;
Papakonstantinou et al., 2021; Pinto et al., 2021), as well as the abun­
dance of floating litter (items/km[2]) (de Vries et al., 2021). All related
papers can be seen in Table 2 (papers with the tag “Litter assessment” in
the “Usability” column), as well as on the online database. Additionally,
four studies have been found to process litter video footage to detect and
count litter items (Armitage et al., 2022; Kylili et al., 2021; Teng et al.,
2022; van Lieshout et al., 2020), indicating the potential of the auto­
mated counting of litter items in operational surveys. Finally, the
extended coverage area of satellites favored the analysis of
satellite-based litter imagery in extended geographic sites around the
world (Fig. 5).

_7.1. Performance of AI algorithms_

AI algorithms generally achieved high accuracy (>70%) when they
performed binary classifications of litter images, such as debris vs. water
(Sannigraphi et al., 2022), plastic vs. non-plastic (Jamali and Mah­
dianpari, 2021), animal vs. litter (Moorton et al., 2022), the presence or
absence of plastics (Armitage et al., 2022), clean vs. polluted images
(Chang et al., 2020), or litter vs. water (Sannigraphi et al., 2022).
Moderate-to-good performance was also achieved for the classification
and detection macrolitter images both for in-situ (Cortesi et al., 2022;
Gonçalves et al., 2020a; Veerasingam et al., 2022; Watanabe et al.,
2019) and public (Cordova et al., 2022´ ; Fulton et al., 2018; Hong et al.,
2020a; Kylili et al., 2019; Majchrowska et al., 2022; Panwar et al., 2020;
Priyadarshini et al., 2022; Tata et al., 2021) datasets. In contrast, im­
agery with complex natural backgrounds and small datasets tended to
show moderate overall performance (Lavender, 2022; Martin et al.,
2018, 2021; Politikos et al., 2021).
AI studies with satellite imagery tended to perform pixel-based
classification and detection of macrolitter items. Contrary, objectbased detection methods were increasingly used in non-satellite data­
sets. This pattern can be partially explained by the relative size of litter
items compared to the resolution of the processed images. The type and
characteristics of a litter item are often barely visible (just a few pixels)
in satellite images (e.g., Basu et al., 2021; Biermann et al., 2020; Kikaki
et al., 2022). So, using bounding box annotation of these images
(annotation for object-based predictions) didn’t seem to be an efficient
way to train the corresponding CNN-based semantic segmentation ar­
chitectures. Instead, spectral analysis was used in several cases (e.g.,
Biermann et al., 2020; Booth et al., 2022; Themistocleous et al., 2020) to
extract features from the images and then process them with machine
learning algorithms. This was proved efficient to differentiate marine
litter/plastics from other classes (e.g., sea foam, seawater, ship).
To attain the highest possible predictive scores, many studies tested
different algorithms on the same dataset, showing variant performance
(Chin et al., 2022; Fulton et al., 2018; Kikaki et al., 2022; Maharjan
et al., 2022; Martin et al., 2021; Mifdal et al., 2021; Nazerdeylami et al.,
2021; Papakonstantinou et al., 2021; Priyadarshini et al., 2022; Sasaki
et al., 2022; Tata et al., 2021; Tharani et al., 2020; Wolf et al., 2020; Xue
et al., 2021a, b). More recent algorithms tended to have better perfor­

–
mance within a range of 10% 30%, without, however, allowing to
conclude that there is a “winner” algorithm that should be adopted in
future works. Instead, trying several algorithms remains a good practice.
Additionally, the performance of the algorithms was found to be
litter-specific in several studies (Martin et al., 2018; Panwar et al., 2020;
Pinto et al., 2021; Politikos et al., 2021; Song et al., 2021; Valdene­
gro-Toro, 2016; Wolf et al., 2020; Xue et al., 2021), indicating that the
properties of a litter item (e.g., type, shape, size) and its natural back­
ground can be key factors for achieving correct predictions. A general
conclusion about which litter items have a better chance of being pre­
dicted correctly could not be safely extracted from the analysis. An


7


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Fig. 4. World (upper) and European (lower) geographic distribution of AI studies that used regional marine macrolitter datasets collected from in-situ surveys**
(without including satellite data) for their analysis.

**Fig. 5. World geographic distribution of AI marine macrolitter studies that used in-situ satellite image data for their analysis.**


overview of the performance of the algorithms in each collected docu­
ment, as computed from the evaluation metrics can be found on the
online dataset (column: “Predictability”).


Exploratory studies have mainly used MLA and FFNN to predict
floating and beached litter abundance/density using a diverse list of
predictors, such as depth, slope, distance from cities and rivers, waves,


8


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Fig. 6. Number of publications per content category. We note that multiple tags were possible within a reviewed document for the content categories:** “Litter
domain, “Sampling system”, “Task”, “Architecture” and “Usability”. This implies that the frequency numbers of these categories can sum over the total number of
surveyed documents (n = 80).

**Fig. 8. Frequency distribution of publications at the intersection of** “Litter

**Fig. 7. Frequency distribution of publications at the intersection of** “Litter domain” and “Task” content categories.
domain” and “Dataset source” content categories.

source of data in monitoring programs (UNEP, 2021; Canals et al.,
2021), we believe that this kind of studies should be further developed in

tides, currents, wind speed, vegetation coverage, isolation, beach the future.
exposure, and marine traffic density (Franceschini et al., 2019; Kaan­
dorp et al., 2022; Martin et al., 2021). Schulz and Matthies (2014)
selected season, tangled nets, strapping bands, and crisp and sweet _7.2. Limitations_
packaging, as input variables to explain beached litter abundance for
several source categories (plastic, fishing, shipping, and tourism). Their The present review also identified several limitations. Data collection
success (observed vs. predicted litter quantity) was variable, ranging and assessment are at the core of marine litter monitoring. Promoting
from good (R[2 ]> 0.5: Franceschini et al., 2019; Pearson correlation >0.6: the automatic assessment of marine litter should the goal of an AI
Kaandorp et al., 2022) to moderate (R[2 ]= 0.23: Martin et al., 2021; R[2 ]< application on this domain. Nevertheless, limited progress has been
0.4: Schulz and Matthies, 2014), likely implying that some critical achieved in this direction. The majority of publications (80.2%) focused
explanatory variables have not been considered. Given that the in-situ either on fine-tuning and evaluating the performance of existing algo­
collection of macrolitter items on the beaches and seafloor is a main rithms on their imagery or on modifying these architectures with new

branches, in an attempt to get better results (Table 2, papers with the tag

9


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


“PPA” in the “Usability” column). AI-macrolitter assessment was limited
to three studies for floating litter (de Vries et al., 2021; Garcia-Garin
et al., 2021; van Lieshout et al., 2020), whereas it was more active for
beached litter (Table 2, tag “Litter assessment” in the “Usability” col­
umn). This can be attributed to the fact that the acquisition of beached
litter data is a relatively low-cost process with aerial surveying from
land. In contrast, the collection of floating and seafloor litter data re­
quires the use of research vessels in the open sea, implying high oper­
ational costs.

29.3% of the reviewed documents used publicly available imagery
for their analysis (Table 2; papers with the tag “Public” in the “Data

source”
column). Although public datasets have the benefit of resolving
the problem of expensive data collection and image labeling, they don’t
have a practical usability in litter assessment, since in several datasets
litter items were collected in controlled setups, i.e., with only one
instance of litter per image or taken in indoor scenarios. However, this is
rare in real-world marine environments. So, the added value of these
studies lies mainly in testing the predictive capabilities of the algo­
rithms. This pattern indicates a discrepancy; while there is an increasing
number of scientists who seek to advance AI in marine litter research,
the limited availability of real datasets hinders this potential, which in
turn confines the geographic extension of real-world AI litter applica­
tions, especially for non-satellite data. Interestingly, some authors
overcame the lack of data by conducting experimental releases of
macrolitter in specific areas (15.9% of articles; Table 2, tag “Experi­
mental” in the “Dataset source” column), but, again, this didn’t
contribute to the automatic litter assessment.

_7.3. Challenges_

Review analysis illustrated the diverse challenges that authors
encountered during the implementation of AI algorithms. Litter imagery
often contains small or/and imbalanced (low number of samples for
some litter classes) datasets (Booth et al., 2022; Cordova et al., 2022´ ;
Duarte et al., 2020; Gomez et al., 2022´ ; Politikos et al., 2021; Song et al.,
2021). This may affect the training process of the algorithms, often
leading to overfitting,[14 ]which in turn may imply poor performance on
new, unseen data. To partially resolve this issue, data augmentation
techniques are commonly adopted to artificially increase the size of
training data (Aleem et al., 2022; de Vries et al., 2021; Politikos et al.,
2021; Tata et al., 2021; Teng et al., 2022) to prevent overfitting. Duarte
et al. (2020) conducted oversampling to increase the minority class
(litter) to match the same amount of no litter samples, and Nazerdeylami
et al. (2021) merged in-situ with public datasets to increase the per­
formance of adopted algorithms. In parallel, the need for collecting
bigger training samples to attain better classification and detection re­
sults has been highlighted (Basu et al., 2021; van Lieshout et al., 2020;
Papakonstantinou et al., 2021).
Litter identification in real-world marine environments constitutes a
very challenging task for AI algorithms. The automated recognition of
beached/dune litter may be affected by complex natural backgrounds
such as vegetation, the presence of natural wood litter and seashells
among litter items (Andriolo et al., 2022; Gonçalves et al., 2020a;
Nazerdeylami et al., 2021; Song et al., 2021). On the seafloor, litter
items are often degraded, semi-buried or may be found within seagrass
or among rocks to such an extent that they are hardly distinguishable
even by human observers, or they are (Fulton et al., 2019; Politikos
et al., 2021). In addition, litter objects may have huge intraclass vari­
ability (same type but different shape, e.g., bag) and interclass similarity
(e.g., cloth and plastic segment), and this may affect predictability (Xue
et al., 2021a, b). In satellite images, high cloud coverage or false

14 Overfitting happens when a model learns too closely the details and the
noise of the training set to the extent that it cannot generalize enough to make
good predictions on new, unseen data.


annotations by experts in complex cases (e.g., ship vs. wake) can infer
mispredictions of floating items (Mifdal et al., 2021; Kikaki et al., 2022).
Moreover, the spatial resolution of the satellite images has specific
specifications (e.g., Sentinel-2 image is equal to10 m). Although smaller
plastic targets can be discriminated and identified under specific con­
ditions (e.g., 3 m × 10 m in Themistocleous et al., 2020), satellite data
can be mainly used for the detection/monitoring of large-size litter
(Jamali and Mahdianpari, 2021). False predictions may also occur when
litter items have similar spectral signatures and where low concentra­
tions compared to the background signal (Lavender, 2022).
The collection of good quality images of litter is also critical for a
successful task. For instance, the distance between a sampling system
and an object may affect the correct classification of both beached/dune
(Ge et al., 2016; Gonçalves et al., 2020a) and floating (Cortesi et al.,
2022; Watanabe et al., 2019) litter, since with higher altitudes, it may be
difficult to identify objects due to various water surface conditions,
beached landscapes or color and size of targets. Jakovljevic et al. (2020;
floating litter) and Hidaka et al. (2022); beached/dune litter) noted that
the decreased spatial resolution of an image compared to the detectable
litter size may affect accuracy in model predictions. Similarly, Armitage
et al. (2022) underlined that the object detection of floating litter items
can be affected when they have a low pixel percentage within an image,
suggesting cropping the image to smaller ones. A good orientation is also
needed for a camera to take a clear picture of the seafloor marine litter
and avoid a loss in model (Chin et al., 2022). Furthermore, aerial surveys
should be conducted in favorable weather conditions, such as calm
wind, absence of fog, mist, and rain and weak sunlight reflections
(Andriolo and Gonçalves, 2022; Fallati et al., 2019; Garcia-Garin et al.,
2021; Takaya et al., 2022) to collect good quality data.
The advancements, current limitations and challenges identified
from the use of AI in marine macrolitter research are summarized in

Table 4.

_7.4. Future directions_

AI has a tremendous toolkit that could be potentially used in the
future for marine macrolitter research. For instance, Vision Trans­
formers (ViTs) have emerged as an alternative to CNNs that are the most
widely used networks in image recognition tasks (Dosovitskiy et al.,
2021). ViTs extract patches from images and feed them into a trans­
former encoder to obtain a global representation, which will finally be
used for classification. Additionally, unsupervised deep learning tech­
niques, such as SCAN (Van Gansbeke et al., 2020) and DeepDPM (Ronen
et al., 2022), have been proposed for automatically grouping images into
semantically meaningful clusters when image labels are absent. As CNNs
require thousands of annotated images to be trained before generalizing
their learning to unseen scenarios, unsupervised learning could elimi­
nate the time needed for image labeling and, hence, significantly speed
up the classification process. Basu et al. (2021) and Taggio et al. (2022),
used both classification and common unsupervised algorithms referring
to clustering (K-Means and Fuzzy C-Means) to identify plastic litter from
satellite images. Although clustering methods achieved lower perfor­
mance compared to classification, these studies constitute a starting
point towards this direction.
A common and effective strategy to overcome the limited size of
training data is transfer learning, where knowledge gained from one task
is used on a new problem of interest (Pan and Yang, 2010). The idea is to
reuse a previously learned network that has been pre-trained on a very
large dataset (e.g., ImageNet[15]) to improve prediction in the new task,
even if the dataset is small. For instance, transfer learning showed
significantly better classification performance on test images of marine
litter (Martin et al., 2021). Furthermore, the geographical transferability

15 A large dataset, which contains 1.2 million training images from 1000
[classes (https://www.image-net.org/).](https://www.image-net.org/)


10


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


**Table 4**

Overview of advancements, current limitations, challenges, and future di­
rections identified from the use of AI in marine macrolitter research.

**Advancements**

 Automated classification, object detection, and segmentation of marine macrolitter
imagery with AI is feasible.

 AI has made its first steps towards supporting automated litter assessment from insitu surveys.

 - Very good performance of AI algorithms on binary (polluted vs. non polluted)
classification of images.

 - Good performance of AI algorithms on classifying and detecting beached/dune,
floating and seafloor litter for several case studies.

 - Machine learning algorithms achieved, although with variant performance, to
identify the impact of environmental and anthropogenic variables on shaping
macrolitter abundance/density on the beach and seafloor.

 - AI has the tools to process video footage for litter monitoring.

 - Extended geographic coverage of AI applications with in-situ satellite data.

**Limitations**

 - Moderate-to-good performance of AI algorithms on detecting beached/dune,
floating and seafloor litter for small size and complex datasets.

 - Limited geographic distribution of AI applications with in-situ, non-satellite data.

 - Limited use of AI to support litter assessment goals.

 - Complex natural backgrounds (e.g., grass, rocks), complex properties of litter items
(e.g., type, shape, size) and conditions of data acquisition (e.g., image resolution,
weather, flight altitude of optical devices) may deceive the performance of AI
algorithms.

 - Small or imbalanced datasets may deceive the performance of AI algorithms.

 - The resolution of satellite-based images (10 m × 10 m) limits the detection to large

macrolitter items.

**Challenges**

 - Handling of small and imbalanced datasets.

 Improve classification and detection of macrolitter found in complex environments
and those having interclass similarity (e.g., cloth and bag) or intraclass variability (e.
g., a bag and a portion of the bag can have different shape).

 - Acquisition of good quality data.

**Future directions**

 - Collection of bigger and more balanced datasets.

 - Promote geographic transferability of AI-marine litter studies.

 - Explore the use of alternative, state-of-the-art AI architectures.

 - Closer collaboration between computer scientists and marine scientists to design a
vision plan.

of a trained algorithm from one location to another is important since it
is time-consuming and costly to generate location training litter data
(Duarte et al., 2020). The studies of Maharjan et al. (2022), Papakon­
stantinou et al. (2021), and Topouzelis et al. (2021) have contributed to
the transferability of their methods to new and unknown macrolitter
imagery. Further initiatives to compile in-situ datasets from different
regions, retrain state-of-the-art algorithms in the resulting big datasets,
and test them in different sites can potentially broaden the applicability
of AI-marine litter studies and improve their performance.

_7.5. Policies, management, and governance_

In terms of management, public policy, and governance support, the
potential of AI is significant. Global initiatives are numerous and include
the marine Litter platforms from G7 and G20 (Chen, 2015; Vince and
Hardesty, 2018; UNEP, 2021), regional action plans of the regional seas
conventions associated with UNEP, coordinated by the Global Partner­
ship on Marine Litter (GPML), and in Europe, the Marine Strategy
Framework Directive, which includes a monitoring program and a
mitigation action plan. Monitoring plans are all based on the collection
of standardized and harmonized data, according to similar protocols,
with some indicators under development, based on imagery, especially
for floating objects or on the bottom. This is how EMODnet Chemistry
has collected marine litter data since 2016, including data in a large,
consolidated infrastructure guarantees metadata completeness, adopt­
ing different strategies for the management of the diverse litter data


types, exploiting the advantages deriving from the application of the
FAIR (Findability, Accessibility, Interoperability, and Reusability)
principles in marine litter data stewardship (Partescano et al., 2021).
More recently, an international negotiation has been initiated in
order to establish, in 2024, a legally binding convention to limit plastic
pollution[16 ] (Wang, 2023), with GPML to organize, in parallel, various
communities of practices in a UN digital platform,[17 ]in order to support
the integration and harmonizing data and databases, promoting new
approaches to support global monitoring, including new indicators
based on imagery (satellites, video) to support evaluations of both trends
in mounts of litter, and the efficiency of reduction measures.
In fine, the programs of the ocean decade and the EU horizon Europe
Mission “Restore our Oceans and Waters”, are aimed at launching an
ocean twin, in order to manage both data and analyzing tools. It will
include a component dedicated to the marine litter; something that
cannot be dissociated from the current and future developments of
artificial intelligence, as it is the essence of the development of digital
tools.

_7.6. AI micro-litter/plastic research_

AI has been used in laboratory microlitter research as well for
detecting and counting collected micro-plastics/fibres and determining
their size and chemical nature. As it was out of our scope to make a
review of these studies, we mention a few examples for illustration
purposes. Lorenzo-Navarro et al. (2021) used a neural network to
automatically count and classify microplastics (1–5 mm) into three
different shape categories (fragments, pellets, and lines) using pictures
taken with a digital camera and a mobile phone. Deep learning archi­
tectures were applied in scanning electron microscopy images for se­
mantic segmentation of micro-plastics/fibres in the range of 50 μm-1mm
(Shi et al., 2022). In addition, microscope holographic images were
processed with machine learning methods for identifying microplastics
inside heterogeneous pretreated water samples (Bianco et al., 2020).
Massarelli et al. (2021) developed a computer vision and machine
learning system to automatically count and classify microplastics in four
morphology (fragment, pellet, line, fibre) and size (<500 μm, 500–1000
μm, 1000–2000 μm, and 2000–5000 μm) categories. Other studies
combined machine learning with Fourier-transform infrared spectros­
copy (FTIR) spectra to distinguish different polymer types in the
examined microplastic samples (Hufnagl et al., 2022; Kedzierski et al.,
2019). Further microplastics segmentation analysis based on various
deep learning models was reported in Park et al. (2022).

**8. Conclusions**

This review illustrated the developments that have been made in the
domain of macrolitter monitoring and assessment using AI methodolo­
gies. Results showcased that AI has achieved significant progress over
the last few years to provide automatic and scalable solutions for
detecting and classifying macrolitter in all marine landscapes. Concur­
rently, the wide use of AI algorithms on various case studies helped us to
acquire significant knowledge about their capabilities and limitations in
such complex and peculiar imagery. Further progress is needed, how­
ever, to shift from technical implications of the tested algorithms,
mainly presented in the collected literature, towards methodologies that
will meet the needs of the marine litter research community for the
automated assessment of litter distribution and quantities. Additionally,
promoting the collection of big litter data from realistic environments
and the transferability of gained knowledge from one location to another
will further support this goal. Finally, initiatives that will bring closer

16 [https://www.un.org/en/delegate/nations-sign-end-global-scourge-plastic-](https://www.un.org/en/delegate/nations-sign-end-global-scourge-plastic-pollution)
[pollution.](https://www.un.org/en/delegate/nations-sign-end-global-scourge-plastic-pollution)

17
[https://wedocs.unep.org/handle/20.500.11822/37070.](https://wedocs.unep.org/handle/20.500.11822/37070)


11


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


computer scientists and marine scientists to design a vision plan how AI
will contribute on this theme more effectively in the future is a crucial

step.

**Declaration of competing interest**

The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.

**Data availability**

No data was used for the research described in the article.

**Appendix**


**Acknowledgments**

We express our great appreciation to the two reviewers for taking the
time to carefully read the manuscript. Their valuable comments signif­
icantly improved the quality of the manuscript. The authors declare that
they have no known competing financial interests or personal re­
lationships that could have appeared to influence the work reported in
this paper. This research did not receive any funding.


In this Appendix, we provide a brief overview of key ML/DL concepts and methods with a special focus on those that have been adopted in marine
litter research and found in the collected literature. Interested readers should consult introductory texts (Chollet, 2017; Harrison, 2019) to deepen
their understanding.

_Machine learning algorithms_

ML is a subfield of AI that includes a large set of algorithms and heuristics that computer systems use to find complex patterns in data without
explicit programming (Alpaydın, 2014). In ML, the two most common approaches, applied to real-world datasets, are supervised and unsupervised
learning.[18 ]Supervised learning requires a labeled dataset and training of the algorithm system to gain experience; the algorithm is then used to make
predictions on a new dataset. The most common supervised tasks are classification and regression. Classification aims to assign data to specific classes.
For example, in the case of predicting if a transaction is a fraud or not based on several numeric and categorical data (e.g., card number, product value,
device used for the transaction, e-mail of the purchaser), the algorithm system would be provided with many transactions that have already been
labeled as either being fraud or not. At first the algorithm Is trained and validated with the labeled transactions and then tested with new unlabeled
ones. Regression aims to predict a numeric value of interest, called target variable (e.g., temperature, age, salary, price, etc.) based on a list of
dependent variables that are considered as potential drivers of the target variable. To do so, a training set is used to train a regressor and the test set is
used to evaluate the performance of the trained model. In unsupervised learning, the algorithm system is provided with unlabeled data to find
structures on its own. The most common unsupervised tasks are clustering (grouping of data items into clusters based on their similarities or dif­
ferences), dimensionality reduction (filtering of non-important variables in a given dataset), association rule mining (finding of meaningful re­
lationships between variables in a given dataset), outlier/anomaly detection (detection of data items that deviate from a dataset’s normal behavior)
and density estimation (estimation of a continuous density field from discretely sampled data items) (Han et al., 2011). ML algorithms can generally
handle all types of data, namely tabular, images, videos, or documents (Sarker, 2021).

_Neural networks_

DL is a subdomain of ML that uses deep neural networks to imitate human learning and inference to analyze data on a large scale. DL functions by
mimicking the neural connections made in the human brain (Goodfellow et al., 2015). A feedforward neural network (FFNN) is the simplest type of
neural network. FFNN learns the relationship between independent variables that serve as inputs to the network, and dependent variables that serve as
outputs of the network (Fig. A1). For example, if we would like to predict whether it will rain tomorrow based on humidity, temperature and wind
speed, the inputs to the network would be the values of these three variables and the output would be if we would have rain or not. FFNNs are made up
of several layers of interconnected nodes, each of which improves the network’s predictability. These interconnections are not all equal. Instead, each
connection may have a different strength, quantified by learnable parameters, called weights. Weights are updated during the training phase of the
network according to a cost function that minimizes the differences between the network outputs and the known ‘true’ outputs. Final weights encode
the overall knowledge of the network and are used to make predictions of unseen data points. FFNN is generally suited for supervised learning with
large numerical datasets, though it is less effective with image data since it cannot consider the spatial dependencies of features in an image, while it
cannot be used with sequential data (time series, text) because it has no memory of the input it receives and hence it’s unable to predict what’s coming
next. This brings us to the more advanced classes of neural networks that will be discussed in the following subsections.

_Image classification_

Image classification is the task of identifying what an image represents, say, a bottle, a bag, a cup, or a can (Fig. 2a). Image classification was one of
the first areas in which DL made a major contribution to computer vision.[19 ] Convolutional Neural Networks (CNNs) are the most representative
networks designed for image classification (Chen et al., 2021). The main components of a CNN are the convolutional layer, the pooling layer, the
nonlinear activation layer, and the fully connected layer. First, an image is fed into a CNN through the input layer. Then, it is processed through a stack
of alternately arranged convolutional, pooling, and activation layers, and finally it is classified by fully connected layers (Fig. A1). Contrary to

18 Other approaches are semi-supervised learning and reinforcement learning (Sarker, 2021).
19 Computer vision is a field of artificial intelligence that trains computers to interpret and understand the visual world.

12


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

traditional ML classification methods, from which image features are extracted manually, CNNs follow an end-to-end approach, in which only the
image is an input, while the whole learning process is carried out in the network to identify simple shapes (edges, lines, etc.) in the first layers, to more
sophisticated patterns in the next layers, and classes of objects in the final layers. What makes CNNs popular is their efficiency in capturing the spatial
interaction between adjacent pixels in an image and determining which features (e.g., the neck of a bottle) are most important in differentiating one
litter from another. Over the last years, researchers have come up with several, well-established CNN architectures, for instance, AlexNet (Krizhevsky
et al., 2012), VGGNet (Simonyan and Zisserman, 2014) and Inception (Szegedy et al., 2014). For more details about CNNs, the reader is referred to the
recent review paper by Chen et al. (2021).
Other CNN-based architectures that can be used, among others, for image classification are encoder-decoder networks (Badrinarayanan et al.,
2017; Hong et al., 2019). An encoder-decoder architecture consists of a pair of two connected networks (e.g., feed forward neural networks, CNNs): an
encoder model and a decoder model. For computer vision tasks, the encoder is used to learn a compressed representation of the input image (also
called latent space) in such a way that the decoder can reconstruct the original image as closely as possible to the original (Fig. A1). Once the
encoder-decoder is trained and validated, the decoder is discarded, and the encoder is used for the classification task.

_Object detection_

Object detection is a computer vision task that involves both classifying and localizing objects within an image (Fig. 2b). More specifically, object
detection aims to determine whether there are any objects from given categories (e.g., bag, bottle, paper, can, cup, etc.) and, if present, to return the
spatial location of each object, wrapped by a bounding box (Liu et al., 2019).
Object detection has been approached by two main types, namely two-stage and one-stage detectors. Two-stage detectors use a sliding window to
generate candidate object region proposals in an image during the first stage, and then classify and localize them during the second stage. The core
architecture of these detectors includes an agnostic region proposal module coupled with a CNN to convert detection into classification and locali­
zation problems. Single-stage detectors skip the region proposal stage step and classify and localize semantic objects in a single shot, using a dense
sampling of possible locations of various scales and aspect ratios (Elgendy, 2020). In the literature, an extended list of object detection architectures
can be found both for two-stage detectors (e.g., R–CNN [Girshick et al., 2014]) and one-stage detectors (e.g., SSD [Liu et al., 2016], YOLO [Redmon
et al., 2016], EfficientDet [Tan et al., 2020]). The different algorithms attempt to add or modify branches in their architecture to extract efficient
features from the images that will improve their detection capability. For more details on object detection networks, the reader is referred to the recent
review papers by Liu et al. (2019) and Zaidi et al. (2021).

_Instance segmentation_

Instance segmentation is a further extension of object detection, creating a pixel-wise mask for object(s) found in an image (Fig. 2c). Contrary to
object detection, which returns bounding boxes that are always rectangular and hence cannot determine the shape of objects, instance segmentation
can provide more quantitative information about the object(s), estimating their surface area or perimeter. In these networks, an instance mask branch
is usually added in parallel to the classification and bounding parts of object detection architectures. Well-known deep learning architectures that have
been developed to resolve this topic are, among others, Mask R–CNN (He et al., 2017), PANet (Liu et al., 2018), and YOLACT (Bolya et al., 2019). For
more details about instance segmentation and the aforementioned networks, the reader is referred to the recent review by Hafiz and Bhat (2020).

_Semantic segmentation_

Object-based semantic segmentation is also a significant topic in computer vision, where the goal is to assign a class label to each pixel in the image
(Fig. 2d). This task is commonly referred to as “dense prediction”. Semantic segmentation is useful in several tasks, as for example in autonomous
driving to locate frontal objects (roads, vehicles, pavements, humans) (Kaymak and Uçar, 2019) and medical image diagnostics (Liu et al., 2021). A
variety of deep learning architectures (e.g., fully convolutional networks encoder-decoder models, attention-based models, recurrent neural
network-based models, dilated convolutional models) have been proposed in the literature to resolve this task. Indicatively, well-known architectures
designed for semantic segmentation are ReSeg (Visin et al., 2016), SegNet (Badrinarayanan et al., 2017), and DeepLab (Chen et al., 2017). For more
details on the semantic segmentation architectures, the reader is referred to the recent review papers by Minaee et al. (2020) and Mo et al. (2022).

13


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Fig. A1. Schematic diagram of Feed Forward Neural Network, Convolutional Neural Network (CNN) and Encoder-Decoder architecture.**

Evaluating the performance of a ML-DL algorithm is essential for measuring its predictive accuracy. For instance, a computer system should be
efficient to distinguish between categories, e.g., bottle and. Bag. For (image) classification tasks, the most common evaluation metrics are accuracy,
recall, precision, and F1-score (Fig. 2). For evaluating a segmentation task, the two common metrics are: mean Average Precision (mAP) and
Intersection Over Union (IoU) (Fig. 2). The closer all these metrics are to one, the better and more accurate the performance of that model. Finally,
regression tasks are commonly evaluated through the metrics of Mean Square Error (MSE), Mean absolute Error (MAE), Root Mean Square Error
(RMSE) and R[2]. A short description of the evaluation metrics along with their formulas are shown in Table A1.

**Table A1**

Metrics for evaluating the performance of AI algorithms.

Metric (Task) Description Formula

Accuracy (Acc) Fraction of correct classifications out of the total number of classifications. _Acc =_ _TP + TN_
(Classification) _TP + FP + TN + FN_ _[,]_

TP: True positives
TN: True negatives
FP: False positives
FN: False negatives
Precision (P) (Classification) Fraction of true positive classifications over the sum of true positive and false positive classifications. _P =_ _TPTP + FP_ _[,]_

TP: True positives
FP: False positives
RecallI) Fraction of true positive classifications over the sum of true positive and false negative classifications.
(Classification)

(continued on next page)

14


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_

**Table A1 (continued** )

Metric (Task) Description Formula

_TP_
_R =_
_TP + FN_ _[,]_

TP: True positives
FN: False negatives
F1 score (F) (Classification) F1 score is a unified metric, computed as the harmonic mean of precision and recall. _F = 2_ _[P][ ∗]_ _[R]_
_P + R_ _[,]_

P: precision, R: recall
mAP (Object detection, mAP (mean Average Precision) shows how well the predicted box matches the ground truth (localization), and _mAP =_ [∑][N]i=1[AP][i][,]
Segmentation) whether the class label is correctly predicted (classification).

_AP =_ ∫01 _[P][(][R][)][dR][,]_
AP (Average precision) value is the mean value of the precision value under different recalls P: precision, R: recall and

N: the total number of data

instances
IoU (Object detection, IoU (Intersection Over Union) measures the percent overlap between the correct region (ground truth) and the _IoU =_ [Area of Overlap]
Segmentation) classified region (algorithm output). IoU ranges between 0 and 1, with 0 signifying no overlap and 1 signifying a _Area of Union_
perfect overlap.

MSE, MAE RMSE, R2 (Regression) Mean Squared Error (MSE), Mean absolute Error (MAE) and Root Mean Square Error (RMSE) represent various ways to measure the error difference between ground truth observations ( ̂yi ) and predictions (yi). _MSE =_ _N[1]_ ∑Ni=1[(][y][i][ −] _ŷi_ )[2 ]
an outcome. RCoefficient of determination (R[2 ]closer to 1 imply a better prediction. [2]) is a number between 0 and 1 that measures how well a statistical model predicts _MAE =_ _N[1]_ ∑̅̅̅̅̅̅̅̅̅̅Ni=1⃒⃒yi − _ŷi_ ⃒⃒2

RMSE = √MSE

_N_ ̂

_R[2]_ = 1 − ∑i=N1[(][y][i][ −] _yi_ )[2]

∑i=1[(][y][i][ −] _[y][)][2 ]_

N: total number of

observations

_y: average value of predictions_

N: total number of data

instances

**References** [multispectral Sentinel-2 remote sensing imagery. Rem. Sens. 13, 1598. https://doi.](https://doi.org/10.3390/rs13081598)

[org/10.3390/rs13081598.](https://doi.org/10.3390/rs13081598)

Acuna Ruz, T., et al., 2018. Anthropogenic marine debris over beaches: spectral [Bianco, V., et al., 2020. Microplastic identification via holographic imaging and machine learning. Adv. Intell. Syst. 2, 1900153 https://doi.org/10.1002/aisy.201900153.](https://doi.org/10.1002/aisy.201900153)
characterization for remote sensing applications. Remote Sens. Environ. 217,
[309–322. https://doi.org/10.1016/j.rse.2018.08.008.](https://doi.org/10.1016/j.rse.2018.08.008) Biermann, L., Clewley, D., Martinez-Vicente, V., Topouzelis, K., 2020. Finding plastic
Adamopoulou, A., et al., 2021. Distribution patterns of floating microplastics in open and [patches in coastal waters using optical satellite data. Sci. Rep. 10, 5364. org/10.1038/s41598-020-62298-z.](https://doi.org/10.1038/s41598-020-62298-z) [https://doi.](https://doi.org/10.1038/s41598-020-62298-z)
coastal waters of the eastern Mediterranean Sea (Ionian, Aegean, and Levantine
[Aleem, A., Tehsin, S., Kausar, S., Jameel, A., 2022. Target classification of marine debris seas). Front. Mar. Sci. 8, 699000 using deep learning. Intell. Autom. Soft Comput. 32, 73https://doi.org/10.3389/fmars.2021.699000–85. https://doi.org/](https://doi.org/10.3389/fmars.2021.699000) . [Bolya, D., Zhou, C., Xiao, F., Lee, Y.J., 2019. YOLACT: real-time instance segmentation. SAVE Proc. IEEE Comput. Soc. Conf. Comput. Vis. 915710.1109/ICCV.2019.00925.](https://doi.org/10.1109/ICCV.2019.00925) [–9166. https://doi.org/](https://doi.org/10.1109/ICCV.2019.00925)
[10.32604/iasc.2022.021583.](https://doi.org/10.32604/iasc.2022.021583) Booth, H., Ma, W., Karakus, O., 2022. High-precision density mapping of marine debris
[Alpaydın, E., 2014. Introduction to Machine Learning. MIT Press, p. 640Andriolo, U., et al., 2022. Beached and floating litter surveys by unmanned aerial .](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref5) [Broere, S., van Emmerik, T., Gonzalez Fernandez, D., Luxemburg, W., de Schipper, M., and floating plastics via satellite imagery. arXiv preprint. 0/arXiv.2210.05468.](https://doi.org/10.48550/arXiv.2210.05468) [https://doi.org/10.4855](https://doi.org/10.48550/arXiv.2210.05468)
[vehicles: operational analogies and differences. Remote Sens 14, 1336. https://doi.](https://doi.org/10.3390/rs14061336)
[org/10.3390/rs14061336.](https://doi.org/10.3390/rs14061336) Cozar, A., van de Giesen, N., 2021. Towards underwater aterseriza monitoring using

[echo sounding. Front. Earth Sci. 9, 628704 https://doi.org/10.3389/](https://doi.org/10.3389/feart.2021.628704)

Andriolo, U., Goncalves, G.G., 2022. Is coastal erosion a source of marine litter pollution? [feart.2021.628704.](https://doi.org/10.3389/feart.2021.628704)
[Evidence of coastal dunes being a reservoir of plastics. Mar. Pollut. Bull. 174, 113307 https://doi.org/10.1016/j.marpolbul.2021.113307.](https://doi.org/10.1016/j.marpolbul.2021.113307) Canals, M., et al., 2021. The quest for seafloor macrolitter: a critical review of

background knowledge, current methods and future prospects. Environ. Res. Lett.

Andriolo, U., Goncalves, G., Sobral, P., Fontan Bouzas, A., Bessa, F., 2020. Beach-dune [16, 023001 https://doi.org/10.1088/1748-9326/abc6d4.](https://doi.org/10.1088/1748-9326/abc6d4)
[morphodynamics and marine macro-litter abundance: an integrated approach with Unmanned Aerial System. Sci. Total Environ. 749, 141474 j.scitotenv.2020.141474.](https://doi.org/10.1016/j.scitotenv.2020.141474) [https://doi.org/10.1016/](https://doi.org/10.1016/j.scitotenv.2020.141474) [Chang, M., Xing, Y.Y., Zhang, Q.Y., Han, S.J., Kim, M., 2020. A CNN image classification analysis for 15–26. https://doi.org/10.15722/jds.18.1.202001.15“Clean-Coast Detector” as tourism service distribution. J. Distrib. Sci. 18, .](https://doi.org/10.15722/jds.18.1.202001.15)
Andriolo, U., Goncalves, G., Sobral, P., Bessa, F., 2021a. Spatial and size distribution of

Chen, C.L., 2015. Regulation and management of marine litter. In: Bergman, M., M.,

[macro-litter on coastal dunes from drone images: a case study on the Atlantic coast. Mar. Pollut. Bull. 169, 112490 https://doi.org/10.1016/j.marpolbul.2021.112490.](https://doi.org/10.1016/j.marpolbul.2021.112490) [Gutow, L., Klages, M. (Eds.), Marine Anthropogenic Litter. Springer, pp. 395https://doi.org/10.1007/978-3-319-16510-3.](https://doi.org/10.1007/978-3-319-16510-3) –428.
Andriolo, U., et al., 2021b. Drones for litter mapping: an inter-operator concordance test

Chen, L.-C., Papandreou, G., Kokkinos, I., Murphy, K., Yuille, A.L., 2017. Deeplab:

[in marking beached items on aerial images. Mar. Pollut. Bull. 69, 112542 https://](https://doi.org/10.1016/j.marpolbul.2021.112542)
[doi.org/10.1016/j.marpolbul.2021.112542.](https://doi.org/10.1016/j.marpolbul.2021.112542) [Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected Crfs. https://doi.org/10.48550/arXiv.1606.00915 arXiv](https://doi.org/10.48550/arXiv.1606.00915)
Armitage, S., Awty-Carroll, K., Clewley, D., Martinez-Vicente, V., 2022. Detection and
classification of floating plastic litter using a vessel-mounted video camera and deep preprint.
[learning. Rem. Sens. 14, 3425. https://doi.org/10.3390/rs14143425, 2022.](https://doi.org/10.3390/rs14143425) [Chen, L., et al., 2021. Review of image classification algorithms based on convolutional neural networks. Rem. Sens. 13 (22), 4712. https://doi.org/10.3390/rs13224712.](https://doi.org/10.3390/rs13224712)
Badrinarayanan, V., Kendall, A., Cipolla, R., 2017. Segnet: a deep convolutional encoder
Chin, C.S., Neo, A.B.H., See, S., 2022. Visual marine debris detection using Yolov5s for

[decoder architecture for image segmentation. IEEE Trans. Pattern Anal. Mach. Intell. 39 (12), 2481–2495. https://doi.org/10.1109/TPAMI.2016.2644615.](https://doi.org/10.1109/TPAMI.2016.2644615) [autonomous underwater vehicle. IEEE/ACIS 22nd Int. Conf. Comput. Inf. 20https://doi.org/10.1109/ICIS54925.2022.9882484.](https://doi.org/10.1109/ICIS54925.2022.9882484) –24.
[Bajaj, R., et al., 2021. Sea debris detection using deep learning: diving deep into the sea. IEEE Int. Conf. Intell. Comput. Power Comm. Tech. (GUCON) 1–6. https://doi.org/](https://doi.org/10.1109/GUCON50781.2021.9573722) [Chollet, F., 2017. Deep Learning with Python. Manning Publications, p. 384.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref24)
[Bak, S.H., et al., 2019. Detection and monitoring of beach litter using UAV image and 10.1109/GUCON50781.2021.9573722.](https://doi.org/10.1109/GUCON50781.2021.9573722) Clark, N.J., Khan, R., Mitrano, D.M., Boyle, D., Thompson, R., 2022. Demonstrating the translocation of nanoplastics across the fish intestine using palladium-doped

[polystyrene in a salmon gut-sac. Environ. Int. 159, 06994 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.envint.2021.106994)

[deep neural network. Int. Arch. Photogr. Remote Sens. Spat. Inf. Sci. XLII-3/W8, 55–58. https://doi.org/10.5194/isprs-archives-XLII-3-W8-55-2019.](https://doi.org/10.5194/isprs-archives-XLII-3-W8-55-2019) [envint.2021.106994.](https://doi.org/10.1016/j.envint.2021.106994)
[Balas, C.E., Ergın, A., Williams, A.T, Koc, L., 2004. Marine litter prediction by artificial intelligence. Mar. Pollut. Bull. 48, 449marpolbul.2003.08.020.](https://doi.org/10.1016/j.marpolbul.2003.08.020) [–457. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2003.08.020) [Cocking, J., Narayanaswamy, B.E., Waluda, C.M., Williamson, B.J., 2022. Aerial detection of beached marine plastic using a novel, hyperspectral short-wave infrared (SWIR) camera. ICES J. Mar. Sci. 79 (3), 648fsac006.](https://doi.org/10.1093/icesjms/fsac006) [–660. https://doi.org/10.1093/icesjms/](https://doi.org/10.1093/icesjms/fsac006)
[Balas, C.E., Williams, A.T., Ergin, A., Koç, M.L., 2006. Litter categorization of beaches in Wales, UK by multi-layer neural networks. J. Coast. Res. JCR SI 39, 1516http://www.jstor.org/stable/25743008.](http://www.jstor.org/stable/25743008) –1520. Cordova, M., et al., 2022. Litter detection with deep learning: a comparative study. ´ [Sensors 22 (2), 548. https://doi.org/10.3390/s22020548.](https://doi.org/10.3390/s22020548)
Basu, B., Sannigrahi, S., Basu, A.S., Pilla, F., 2021. Development of novel classification
algorithms for detection of floating plastic debris in coastal waterbodies using

15


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


Cortesi, I., Masiero, A., Tucci, G., Topouzelis, K., 2022. UAV-based river plastic detection
with a multispectral camera. Int. Arch. Photogram. Rem. Sens. Spatial Inf. Sci. 43,
[855–861. https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-855-2022.](https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-151-2022)
de Vries, R., Egger, M., Mani, T., Lebreton, L., 2021. Quantifying floating plastic debris at
sea using vessel-based optical data and artificial intelligence. Rem. Sens. 13, 3401.
[https://doi.org/10.3390/rs13173401.](https://doi.org/10.3390/rs13173401)
Deng, H., et al., 2021. An embeddable algorithm for automatic garbage detection based
[on complex marine environment. Sensors 21, 6391. https://doi.org/10.3390/](https://doi.org/10.3390/s21196391)
[s21196391.](https://doi.org/10.3390/s21196391)

[Deng, Li, Liu, Y., 2018. Deep Learning in Natural Language Processing. Springer, p. 329.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref30)
Dosovitskiy, A., et al., 2021. An image is worth 16x16 words: transformers for image
[recognition at scale. arXiv preprint. https://doi.org/10.48550/arXiv.2010.11929.](https://doi.org/10.48550/arXiv.2010.11929)
Downe-Wamboldt, B., 1992. Content analysis: method, applications, and issues. Health
[Care Women Int. 13 (3), 313–321. https://doi.org/10.1080/07399339209516006.](https://doi.org/10.1080/07399339209516006)
Driedger, A.G.J., et al., 2015. Plastic debris in the Laurentian Great Lakes: a review.
[J. Great Lakes Res. 41 (1), 9–19. https://doi.org/10.1016/j.jglr.2014.12.020.](https://doi.org/10.1016/j.jglr.2014.12.020)
Duarte, D., Andriolo, U., Goncalves, G., 2020. Addressing the class imbalance problem in
the automatic image classification of coastal litter from orthophotos derived from
UAS imagery. ISPRS Ann. Photogramm. Rem. Sens. Spat. Inf. Sci. 3–2020, 439–445.
[https://doi.org/10.5194/isprs-annals-V-3-2020-439-2020.](https://doi.org/10.5194/isprs-annals-V-3-2020-439-2020)
[Elgendy, M., 2020. Deep Learning for Vision Systems. Manning Publications, p. 480.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref35)
Elo, S., Kyngas, H., 2008. The qualitative content analysis process. J. Adv. Nurs. 2 (1),
[107–115. https://doi.org/10.1111/j.1365-2648.2007.04569.x.](https://doi.org/10.1111/j.1365-2648.2007.04569.x)
Eriksen, M., et al., 2014. Plastic pollution in the world’s oceans: more than 5 trillion
plastic pieces weighing over 250,000 tons afloat at sea. PLoS One 9 (12), e111913.
[https://doi.org/10.1371/journal.pone.0111913.](https://doi.org/10.1371/journal.pone.0111913)
Escobar Sanchez, G., Haseler, M., Oppelt, N., Schernewski, G., 2021. Efficiency of aerial
drones for macrolitter monitoring on Baltic Sea beaches. Front. Environ. Sci. 8,
[560237 https://doi.org/10.3389/fenvs.2020.560237.](https://doi.org/10.3389/fenvs.2020.560237)
Fakiris, E., et al., 2022. Insights into seafloor litter spatiotemporal dynamics in urbanized
shallow Mediterranean bays. An optimized monitoring protocol using towed
[underwater cameras. J. Environ. Manag. 308, 114647 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jenvman.2022.114647)
[jenvman.2022.114647.](https://doi.org/10.1016/j.jenvman.2022.114647)
Fallati, L., et al., 2019. Anthropogenic marine debris assessment with unmanned aerial
vehicle imagery and deep learning: a case study along the beaches of the Republic of
[Maldives. Sci. Total Environ. 693, 133581 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.scitotenv.2019.133581)
[scitotenv.2019.133581.](https://doi.org/10.1016/j.scitotenv.2019.133581)

Forrest, A., et al., 2019. Eliminating plastic pollution: how a voluntary contribution from
[industry will drive the circular plastics economy. Front. Mar. Sci. 6, 627. https://doi.](https://doi.org/10.3389/fmars.2019.00627)
[org/10.3389/fmars.2019.00627.](https://doi.org/10.3389/fmars.2019.00627)
Fossum, T.O., 2022. Underwater autonomous mapping and characterization of marine
[debris in urban water bodies. arXiv preprint.. https://doi.org/10.48550/](https://doi.org/10.48550/arXiv.2208.00802)
[arXiv.2208.00802.](https://doi.org/10.48550/arXiv.2208.00802)

[Fotopoulou, K.N., Karapanagioti, H.K., 2017. Degradation of various plastics in the](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref42)
[environment. In: The Handbook of Environmental Chemistry. Springer, Berlin,](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref42)
[Heidelberg, pp. 1–22.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref42)
Franceschini, S., et al., 2019. Rummaging through the bin: modelling marine litter
[distribution using Artificial Neural Networks. Mar. Pollut. Bull. 149, 110580 https://](https://doi.org/10.1016/j.marpolbul.2019.110580)
[doi.org/10.1016/j.marpolbul.2019.110580.](https://doi.org/10.1016/j.marpolbul.2019.110580)
Freitas, S., Silva, H., Silva, E., 2021. Remote hyperspectral imaging acquisition and
[characterization for marine litter detection. Remote Sens. 13, 2536. https://doi.org/](https://doi.org/10.3390/rs13132536)
[10.3390/rs13132536.](https://doi.org/10.3390/rs13132536)
Fulton, M., Hong, J., Islam, M.J., Sattar, J., 2018. Robotic detection of marine litter using
[deep visual detection models. arXiv preprint. https://arxiv.org/abs/1804.01079.](https://arxiv.org/abs/1804.01079)
Fulton, M., Hong, J., Islam, M.J., Sattar, J., 2019. Robotic detection of marine litter using
[deep visual detection models. arXiv preprint. https://arxiv.org/abs/1804.01079.](https://arxiv.org/abs/1804.01079)
Galgani, F., et al., 2000. Litter on the sea floor along European coasts. Mar. Pollut. Bull.
[40, 516–527. https://doi.org/10.1016/S0025-326X(99)00234-9.](https://doi.org/10.1016/S0025-326X(99)00234-9)
Galgani, L., et al., 2019. Editorial: impacts of marine litter. Front. Mar. Sci. 6, 208.

[https://doi.org/10.3389/fmars.2019.00208.](https://doi.org/10.3389/fmars.2019.00208)
Gao, J., Li, P., Chen, Z., Zhang, J., 2020. A survey on deep learning for multimodal data
[fusion. Neural Comput. 32 (5), 829–864. https://doi.org/10.1162/neco_a_01273.](https://doi.org/10.1162/neco_a_01273)
Garcia-Garin, O., et al., 2020a. Who’s better at spotting? A comparison between aerial
photography and observer-based methods to monitor floating marine litter and
[marine mega-fauna. Environ. Pollut. 258, 113680 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.envpol.2019.113680)
[envpol.2019.113680.](https://doi.org/10.1016/j.envpol.2019.113680)
Garcia-Garin, O., et al., 2020b. Floating marine macro-litter in the North Western
Mediterranean Sea: results from a combined monitoring approach. Mar. Pollut. Bull.
[159, 111467 https://doi.org/10.1016/j.marpolbul.2020.111467.](https://doi.org/10.1016/j.marpolbul.2020.111467)
Garcia-Garin, O., et al., 2021. Automatic detection and quantification of floating marine
macro-litter in aerial images: introducing a novel deep learning approach connected
[to a web application in R. Environ. Pollut. 273, 116490 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.envpol.2021.116490)
[envpol.2021.116490.](https://doi.org/10.1016/j.envpol.2021.116490)
Gauci, A., Deidun, A., Montebello, J., Abela, J., Galgani, F., 2019. Automating the
characterization of beach microplastics through the application of image analyses.
[Ocean Coast Manag. 182, 104950 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ocecoaman.2019.104950)
[ocecoaman.2019.104950.](https://doi.org/10.1016/j.ocecoaman.2019.104950)

Ge, Z., et al., 2016. Semi-automatic recognition of marine debris on beaches. Sci. Rep. 6,
[25759 https://doi.org/10.1038/srep25759.](https://doi.org/10.1038/srep25759)
[Gesamp, 2019. Guidelines or the monitoring and assessment of plastic litter and](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref54)
[microplastics in the ocean. In: Kershaw, P.J., Turra, A., Galgani, F. (Eds.), IMO/FAO/](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref54)
[UNESCO-IOC/UNIDO/WMO/IAEA/UN/UNEP/UNDP/ISA Joint Group of Experts on](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref54)
[the Scientific Aspects of Marine Environmental Protection, 99. Rep. Stud. GESAMP](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref54)
[No., p. 130](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref54)


Girshick, R., Donahue, J., Darrell, T., Malik, J., 2014. Rich feature hierarchies for
[accurate object detection and semantic segmentation. arXiv preprint. https://doi.](https://doi.org/10.48550/arXiv.1311.2524)
[org/10.48550/arXiv.1311.2524.](https://doi.org/10.48550/arXiv.1311.2524)
Gnann, N., Baschek, B., Ternes, T.A., 2022. Close-range Remote Sensing-Based Detection
and Identification of Macroplastics on Water Assisted by Artificial Intelligence: A
[Review. Water Res., p. 118902. https://doi.org/10.1016/j.watres.2022.118902](https://doi.org/10.1016/j.watres.2022.118902)
Gomez, A., Scandolo, L., Eismann, E., 2022. A learning approach for river debris
[detection. Int. J. Appl. Earth Obs. Geoinf. 107, 102682 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jag.2022.102682)
[jag.2022.102682.](https://doi.org/10.1016/j.jag.2022.102682)
Goncalves, G., Andriolo, U., Pinto, L., Bessa, F., 2020a. Mapping marine litter using UAS
on a beach-dune system: a multidisciplinary approach. Sci. Total Environ. 706,
[135742 https://doi.org/10.1016/j.scitotenv.2019.135742.](https://doi.org/10.1016/j.scitotenv.2019.135742)
Goncalves, G., Andriolo, U., Pinto, L., Duarte, D., 2020b. Mapping marine litter with
Unmanned Aerial Systems: a showcase comparison among manual image screening
[and machine learning techniques. Mar. Pollut. Bull. 155, 111158 https://doi.org/](https://doi.org/10.1016/j.marpolbul.2020.111158)
[10.1016/j.marpolbul.2020.111158.](https://doi.org/10.1016/j.marpolbul.2020.111158)
Goncalves, G., Andriolo, U., Goncalves, L., Sobral, P., Bessa, F., 2020c. Quantifying
marine macro litter abundance on a sandy beach using unmanned aerial systems and
[object-oriented machine learning methods. Rem. Sens. 12, 2599. https://doi.org/](https://doi.org/10.3390/rs12162599)
[10.3390/rs12162599.](https://doi.org/10.3390/rs12162599)
[Goodfellow, I.J., Bengio, Y., Courville, A., 2015. Deep Learning. MIT Press, p. 433.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref61)
Hafiz, A.M., Bhat, G.M., 2020. A Survey on Instance Segmentation: State of the Art arXiv
[preprint. https://arxiv.org/abs/2007.00047.](https://arxiv.org/abs/2007.00047)
[Han, J., Kamber, M., Pei, J., 2011. Data Mining: Concepts and Techniques, third ed.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref63)
[Springer, p. 740.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref63)
Hardesty, B.D., et al., 2017. Using numerical model simulations to improve the
understanding of microplastic distribution and pathways in the marine environment.
[Front. Mar. Sci. 30, 1–9. https://doi.org/10.3389/fmars.2017.00030.](https://doi.org/10.3389/fmars.2017.00030)
[Harrison, M., 2019. Machine Learning Pocket Reference. O’Reilly Media, Inc.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref65)
Haseler, M., Schernewski, G., Balciunas, A., Sabaliauskaite, V., 2018. Monitoring
methods for large micro- and meso-litter and applications at Baltic beaches. J. Coast
[Conserv. 22 (1), 27–50. https://doi.org/10.1007/s11852-017-0497-5.](https://doi.org/10.1007/s11852-017-0497-5)
[He, K., Gkioxari, G., Dollar, P., Girshick, R., 2017. Mask R-CNN arXiv preprint. htt](https://arxiv.org/abs/1703.06870)
[ps://arxiv.org/abs/1703.06870.](https://arxiv.org/abs/1703.06870)
Helinski, O.K., Poor, C., Wolfand, J.M., 2021. Ridding our rivers of plastic: a framework
[for plastic pollution capture device selection. Mar. Pollut. Bull. 165, 112095 https://](https://doi.org/10.1016/j.marpolbul.2021.112095)
[doi.org/10.1016/j.marpolbul.2021.112095.](https://doi.org/10.1016/j.marpolbul.2021.112095)
Hengstmann, E., Fischer, E.K., 2020. Anthropogenic litter in freshwater environments
study on lake beaches evaluating marine guidelines and aerial imaging. Environ.
[Res. 189 https://doi.org/10.1016/j.envres.2020.109945.](https://doi.org/10.1016/j.envres.2020.109945)
Hong, J., Fulton, M., Sattar, J., 2019. A generative approach towards improved robotic
[detection of marine litter. arXiv preprint. https://doi.org/10.48550/arXiv.1910.](https://doi.org/10.48550/arXiv.1910.04754)
[04754.](https://doi.org/10.48550/arXiv.1910.04754)
Hidaka, M., et al., 2022. Pixel-level image classification for detecting beach litter using a
[deep learning approach. Mar. Pollut. Bull. 175, 113371 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2022.113371)
[marpolbul.2022.113371.](https://doi.org/10.1016/j.marpolbul.2022.113371)
Hong, J., Fulton, M., Junaed, S., 2020. TrashCan: a semantically-segmented dataset
[towards visual detection of marine debris. arXiv preprint. https://doi.org/10.4855](https://doi.org/10.48550/arXiv.2007.08097)
[0/arXiv.2007.08097.](https://doi.org/10.48550/arXiv.2007.08097)
Hufnagl, B., et al., 2022. Computer-assisted analysis of microplastics in environmental
samples based on μFTIR imaging in combination with machine learning. Environ.
[Sci. Technol. Lett. 9, 90–95. https://doi.org/10.1021/acs.estlett.1c00851.](https://doi.org/10.1021/acs.estlett.1c00851)
Ioakeimidis, C., et al., 2014. A comparative study of marine litter on the seafloor of
coastal areas in the Eastern Mediterranean and Black Seas. Mar. Pollut. Bull. 89

[(1–2), 296–304. https://doi.org/10.1016/j.marpolbul.2014.09.044.](https://doi.org/10.1016/j.marpolbul.2014.09.044)
Jakovljevic, G., Govedarica, M., Alvarez-Taboada, F., 2020. A deep learning model for
automatic plastic mapping using unmanned aerial vehicle (UAV) data. Rem. Sens.
[12, 1515. https://doi.org/10.3390/rs12091515.](https://doi.org/10.3390/rs12091515)
Jamali, A., Mahdianpari, M.A., 2021. Cloud-based framework for large-scale monitoring
of ocean plastics using multi-spectral satellite imagery and generative adversarial
[network. Water 13, 2553. https://doi.org/10.3390/w13182553.](https://doi.org/10.3390/w13182553)
JAMSTEC, 2018. Deep-sea Debris Database. Japan Agency for Marine Earth Science and
[Technology. http://www.godac.jamstec.go.jp/catalog/dsdebris/metadataList?lang](http://www.godac.jamstec.go.jp/catalog/dsdebris/metadataList?lang=en)

[=en.](http://www.godac.jamstec.go.jp/catalog/dsdebris/metadataList?lang=en)

Kaandorp, M.L.A., et al., 2022. Using machine learning and beach cleanup data to
explain litter quantities along the Dutch North Sea coast. Ocean Sci. 18, 269–293.
[https://doi.org/10.5194/os-18-269-2022.](https://doi.org/10.5194/os-18-269-2022)
Kako, S., Morita, S., Taneda, T., 2020. Estimation of plastic marine debris volumes on
beaches using unmanned aerial vehicles and image processing based on deep
[learning. Mar. Pollut. Bull. 155, 111127 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2020.111127)
[marpolbul.2020.111127.](https://doi.org/10.1016/j.marpolbul.2020.111127)
Kankane, A., Kang, D., 2021. Detection of seashore debris with fixed camera images
using computer vision and deep learning. 6th Int. Conf. Intell. Inf. Biomed. Sci.
[34–38. https://doi.org/10.1109/ICIIBMS52876.2021.9651572.](https://doi.org/10.1109/ICIIBMS52876.2021.9651572)
Karakus¸, O., 2022. Can we “sense” the call of the ocean? current advances in remote
sensing computational imaging for marine debris monitoring. arXiv preprint.
[https://doi.org/10.48550/arXiv.2210.06090.](https://doi.org/10.48550/arXiv.2210.06090)
Kataoka, T., Nihei, Y., 2020. Quantification of floating riverine macro-debris transport
[using an image processing approach. Sci. Rep. 10, 2198. https://doi.org/10.1038/](https://doi.org/10.1038/s41598-020-59201-1)
[s41598-020-59201-1.](https://doi.org/10.1038/s41598-020-59201-1)

Kataoka, T., Hinata, H., Kako, S., 2012. A new technique for detecting colored macro
plastic debris on beaches using webcam images and CIELUV. Mar. Pollut. Bull. 64
[(9), 1829–1836. https://doi.org/10.1016/j.marpolbul.2012.06.006.](https://doi.org/10.1016/j.marpolbul.2012.06.006)
[Kaymak, C., Ucar, A., 2019. A Brief survey and an application of semantic image](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref84)
[segmentation for autonomous driving. In: Handbook of Deep Learning Applications,](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref84)
[(Edits) Valentina Emilia Balas, Sanjiban Sekhar Roy. Springer, pp. 161–200.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref84)


16


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


Kedzierski, M., et al., 2019. A machine learning algorithm for high throughput
identification of FTIR spectra: application on microplastics collected in the
[Mediterranean Sea. Chemosphere 234, 242–251. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.chemosphere.2019.05.113)
[chemosphere.2019.05.113.](https://doi.org/10.1016/j.chemosphere.2019.05.113)
Kershaw, P., Turra, A., Galgani, F., van Franeker, J.A., 2019. Guidelines for the
monitoring and assessment of plastic litter in the ocean. Rep. Stud. GESAMP No. 99,
[130. https://wesr.unep.org/media/docs/marine_plastics/une_science_dvision_ges](https://wesr.unep.org/media/docs/marine_plastics/une_science_dvision_gesamp_reports.pdf)
[amp_reports.pdf.](https://wesr.unep.org/media/docs/marine_plastics/une_science_dvision_gesamp_reports.pdf)
Kikaki, K., et al., 2022. MARIDA: a benchmark for marine debris detection from Sentinel[2 remote sensing data. PLoS One 17 (1), e0262247. https://doi.org/10.1371/](https://doi.org/10.1371/journal.pone.0262247)
[journal.pone.0262247.](https://doi.org/10.1371/journal.pone.0262247)
[Krippendorff, K., 1980. Content Analysis: an Introduction to its Methodology. Sage](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref88)
[Publications, p. 422.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref88)
Kristollari, V., Karathanassi, V., 2020. Artificial neural networks for cloud masking of
Sentinel-2 ocean images with noise and sunglint. Int. J. Rem. Sens. 41, 4102–4135.
[https://doi.org/10.1080/01431161.2020.1714776.](https://doi.org/10.1080/01431161.2020.1714776)
Krizhevsky, A., Sutskever, I., Hinton, G., 2012. ImageNet classification with deep
convolutional neural networks. Neural Inf. Process. Syst. 25, 1–9, 1097-1105.
[https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a6](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
[8c45b-Paper.pdf.](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)
[Kylili, K., Kyriakides, I., Artusi, A., Hadjistassou, C., 2019. Identifying floating plastic](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref91)
[marine debris using a deep learning approach. Environ. Sci. Pollut. Res. 26,](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref91)
[17091–17099.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref91)

Kylili, K., Artusi, A., Hadjistassou, C., 2021. A new paradigm for estimating the
prevalence of plastic litter in the marine environment. Mar. Pollut. Bull. 173,
[113127. https://doi.org/10.1016/j.marpolbul.2021.113127.](https://doi.org/10.1016/j.marpolbul.2021.113127)
Kylili, K., Hadjistassou, C., Artusi, A., 2020. An intelligent way for discerning plastics at
[the shorelines and the seas. Environ. Sci. Pollut. Res. 27, 42631–42643. https://doi.](https://doi.org/10.1007/s11356-019-05148-4)
[org/10.1007/s11356-019-05148-4.](https://doi.org/10.1007/s11356-019-05148-4)
Lavender, S., 2022. Detection of waste plastics in the environment: application of
[Copernicus earth observation data. Rem. Sens. 14, 4772. https://doi.org/10.3390/](https://doi.org/10.3390/rs14194772)
[rs14194772.](https://doi.org/10.3390/rs14194772)

[LeCun, Y., Bengio, Y., Hinton, G., 2015. Deep learning. Nature 521, 436–444. https://](https://doi.org/10.1038/nature14539)
[doi.org/10.1038/nature14539.](https://doi.org/10.1038/nature14539)
Lin, F., Hou, T., Jin, Q., You, A., 2021. Improved YOLO based detection algorithm for
[floating debris in waterway. Entropy 23, 1111. https://doi.org/10.3390/](https://doi.org/10.3390/e23091111)
[e23091111.](https://doi.org/10.3390/e23091111)

Lin, J.-yu, Liu, H.-t., Zhang, J., 2022. Recent advances in the application of machine
learning methods to improve identification of the microplastics in environment.
[Chemosphere 307, 136092. https://doi.org/10.1016/j.chemosphere.2022.136092.](https://doi.org/10.1016/j.chemosphere.2022.136092)
[Liu, W., et al., 2016. SSD: Single Shot MultiBox Detector. https://doi.org/10.48550/](https://doi.org/10.48550/arXiv.1512.02325)
[arXiv.1512.02325 arXiv preprint.](https://doi.org/10.48550/arXiv.1512.02325)
Liu, S., Qi, L., Qin, H., Shi, J., Jia, J., 2018. Path aggregation network for instance
segmentation. In: Proceedings of the IEEE Conference on Computer Vision and
[Pattern Recognition. CVPR), pp. 8759–8768. https://doi.org/10.48550/](https://doi.org/10.48550/arXiv.1803.01534)
[arXiv.1803.01534.](https://doi.org/10.48550/arXiv.1803.01534)

Liu, L., et al., 2019. Deep Learning for Generic Object Detection: A Survey arXiv preprint.

[https://arxiv.org/abs/1809.02165.](https://arxiv.org/abs/1809.02165)
Liu, X., Song, L., Liu, S., Zhang, Y.A., 2021. Review of deep-learning-based medical
[image segmentation methods. Sustainability 13, 1224. https://doi.org/10.3390/](https://doi.org/10.3390/su13031224)
[su13031224.](https://doi.org/10.3390/su13031224)

Lo, H.-S., Wong, L.-C., Kwok, S.-H., Lee, Y.-K., Po, B.H.-K., Wong, C.-Y., Tam, N.F.-Y.,
Cheung, S.-G., 2020. Field test of beach litter assessment by commercial aerial drone.
[Mar. Pollut. Bull. 151, 110823 https://doi.org/10.1016/j.marpolbul.2019.110823.](https://doi.org/10.1016/j.marpolbul.2019.110823)
Lorenzo-Navarro, J., et al., 2021. Deep learning approach for automatic microplastics
[counting and classification. Sci. Total Environ. 765, 142728. https://doi.org/](https://doi.org/10.1016/j.scitotenv.2020.142728)
[10.1016/j.scitotenv.2020.142728.](https://doi.org/10.1016/j.scitotenv.2020.142728)
Madricardo, F., et al., 2019. Assessing the human footprint on the sea-floor of coastal
[systems: the case of the Venice Lagoon. Italy. Sci. Rep. 9, 6615. https://doi.org/](https://doi.org/10.1038/s41598-019-43027-7)
[10.1038/s41598-019-43027-7.](https://doi.org/10.1038/s41598-019-43027-7)
Maharjan, N., Miyazaki, H., Pati, B.M., Dailey, M.N., Shrestha, S., Nakamura, T., 2022.
Detection of river plastic using UAV sensor data and deep learning. Rem. Sens. 14,
[3049. https://doi.org/10.3390/rs14133049.](https://doi.org/10.3390/rs14133049)
Majchrowska, S, et al., 2022. Deep learning-based waste detection in natural and urban
[environments. Waste Manag. 138, 274–284. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.wasman.2021.12.001)
[wasman.2021.12.001.](https://doi.org/10.1016/j.wasman.2021.12.001)

Mallick, A., Ploger, P., Valdenegro-Toro, M., 2021. Forward-Looking sonar patch ¨
[matching: Modern CNNs, ensembling, and uncertainty. arXiv preprint.. https://doi.](https://doi.org/10.48550/arXiv.2108.01066)
[org/10.48550/arXiv.2108.01066.](https://doi.org/10.48550/arXiv.2108.01066)
Martin, C., et al., 2018. Use of unmanned aerial vehicles for efficient beach litter
[monitoring. Mar. Pollut. Bull. 131, 662–673. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2018.04.045)
[marpolbul.2018.04.045.](https://doi.org/10.1016/j.marpolbul.2018.04.045)
Martin, C., Zhang, Q., Zhai, D., Zhang, X., Duarte, C., 2021. Enabling a large-scale
assessment of litter along Saudi Arabian red sea shores by combining drones and
[machine learning. Environ. Pollut. 277, 116730 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.envpol.2021.116730)
[envpol.2021.116730.](https://doi.org/10.1016/j.envpol.2021.116730)
Massarelli, C., Campanale, C., Uricchio, V.F., 2021. A handy open-source application
based on computer vision and machine learning algorithms to count and classify
[microplastics. Water 13, 2104. https://doi.org/10.3390/w13152104.](https://doi.org/10.3390/w13152104)
Maximenko, N., et al., 2019. Toward the integrated marine debris observing system.
[Front. Mar. Sci. 6, 447. https://doi.org/10.3389/fmars.2019.00447.](https://doi.org/10.3389/fmars.2019.00447)
Merlino, S., Paterni, M., Berton, A., Massetti, L., 2020. Unmanned aerial vehicles for
debris survey in coastal areas: long-term monitoring programme to study spatial and
temporal accumulation of the dynamics of beached marine litter. Rem. Sens. 12,
[1260. https://doi.org/10.3390/rs12081260, 2020.](https://doi.org/10.3390/rs12081260)


Merlino, S., Paterni, M., Locritani, M., Andriolo, U., Goncalves, G., Massetti, L., 2021.
Citizen science for marine litter detection and classification on unmanned aerial
[vehicle images. Water 13, 3349. https://doi.org/10.3390/w13233349, 2021.](https://doi.org/10.3390/w13233349)
Mifdal, J., Longepe, N., Rubwurm, M., 2021. Towards detecting floating objects on a
global scale with learned spatial features using sentinel 2. ISPRS Ann. Photogram.
[Rem. Sens. Spat. Info. Sci. 3–2021, 285–303. https://doi.org/10.5194/isprs-annals-](https://doi.org/10.5194/isprs-annals-V-3-2021-285-2021)
[V-3-2021-285-2021.](https://doi.org/10.5194/isprs-annals-V-3-2021-285-2021)

Mikeli, P., Kikaki, K., Kakogeorgioy, I., Karantzalos, K., 2022. How challenging is the
discrimination of floating materials on the sea surface using high resolution
multispectral satellite data? Int. Arch. Photogram. Rem. Sens. Spatial Inf. Sci. B3[2022 XLIII-, 151. https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-151-2022.](https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-151-2022)
–157.

Minaee, S., et al., 2020. Image Segmentation Using Deep Learning: A Survey arXiv
[preprint. https://arxiv.org/abs/2001.05566.](https://arxiv.org/abs/2001.05566)
Mo, Y., Wu, Y., Yang, X., Liu, F., Liao, Y., 2022. Review the state-of-the-art technologies
of semantic segmentation based on deep learning. Neurocomputing 493, 626–646.
[https://doi.org/10.1016/j.neucom.2022.01.005.](https://doi.org/10.1016/j.neucom.2022.01.005)
Moorton, Z., Kurt, Z., Woo, W.L., 2022. Is the use of deep learning an appropriate means
to locate debris in the ocean without harming aquatic wildlife? Mar. Pollut. Bull.
[181, 113853 https://doi.org/10.1016/j.marpolbul.2022.113853.](https://doi.org/10.1016/j.marpolbul.2022.113853)
Moret Ferguson, S., et al., 2010. The size, mass, and composition of plastic debris in the
[Western North Atlantic Ocean. Mar. Pollut. Bull. 60 (10), 1873–1878. https://doi.](https://doi.org/10.1016/j.marpolbul.2010.07.020)
[org/10.1016/j.marpolbul.2010.07.020.](https://doi.org/10.1016/j.marpolbul.2010.07.020)
Moshtaghi, M., Knaeps, E., 2021. Combining spectral approaches and AI for marine litter
[detection and identification. Int. Geosci. Remote Sens. Symp. 1130–1133. https://](https://doi.org/10.1109/IGARSS47720.2021.9553958)
[doi.org/10.1109/IGARSS47720.2021.9553958.](https://doi.org/10.1109/IGARSS47720.2021.9553958)
Mukonza, S.S., Chiang, J.-L., 2022. Satellite sensors as an emerging technique for
monitoring macro- and microplastics in aquatic ecosystems. Water Emerg. Contam.
[MusiNanoplastics 1, 17. ´c, J., et al., 2020. Detecting underwater sea litter using deep neural networks: an https://doi.org/10.20517/wecn.2022.12.](https://doi.org/10.20517/wecn.2022.12)
[initial study. 5th Int. Conf. Smart Sust. Tech. 1–6. https://doi.org/10.23919/](https://doi.org/10.23919/SpliTech49282.2020.9243709)
[SpliTech49282.2020.9243709.](https://doi.org/10.23919/SpliTech49282.2020.9243709)
Nazerdeylami, A., Majidi, B., Movaghar, A., 2021. Autonomous litter surveying and
human activity monitoring for governance intelligence in coastal eco-cyber-physical
[systems. Ocean Coast Manag. 200, 105478 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.ocecoaman.2020.105478)
[ocecoaman.2020.105478.](https://doi.org/10.1016/j.ocecoaman.2020.105478)

[NOAA, 2014. Report on the Occurrence and Health Effects of Anthropogenic Debris](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref121)
[Ingested by Marine Organisms. Silver Spring, MD, p. 19.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref121)
[NOAA, 2016. Report on Modeling Oceanic Transport of Floating Marine Litter. Silver](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref122)
[Spring, MD, p. 21.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref122)
Ostle, C., et al., 2019. The rise in ocean plastics evidenced from a 60-year time series.
[Nat. Commun. 10, 1622. https://doi.org/10.1038/s41467-019-09506-1.](https://doi.org/10.1038/s41467-019-09506-1)
Pan, S.J., Yang, Q., 2010. A survey on transfer learning. IEEE Trans. Knowl. Data Eng. 22,
[1345–1359. https://doi.org/10.1109/TKDE.2009.191.](https://doi.org/10.1109/TKDE.2009.191)
Panwar, H., et al., 2020. AquaVision: automating the detection of waste in water bodies
[using deep transfer learning. Case Stud. Chem. Environ. Eng. 2, 100026 https://doi.](https://doi.org/10.1016/j.cscee.2020.100026)
[org/10.1016/j.cscee.2020.100026, 2020.](https://doi.org/10.1016/j.cscee.2020.100026)
Papachristopoulou, I., Filippides, A., Fakiris, E., Papatheodorou, G., 2020. Vessel- based
photographic assessment of beach litter in remote coasts. A wide scale application in
[Saronikos Gulf, Greece. Mar. Pollut. Bull. 150, 110684 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2019.110684)
[marpolbul.2019.110684.](https://doi.org/10.1016/j.marpolbul.2019.110684)
Papakonstantinou, A., Batsaris, M., Spondylidis, S., Topouzelis, K., 2021. A Citizen
science unmanned aerial system data acquisition protocol and deep learning
techniques for the automatic detection and mapping of marine litter concentrations
[in the coastal zone. Drones 5, 6. https://doi.org/10.3390/drones5010006.](https://doi.org/10.3390/drones5010006)
Park, H-m., et al., 2022. MP-Net: deep learning-based segmentation for fluorescence
microscopy images of microplastics isolated from clams. PLoS One 17 (6), e0269449.
[https://doi.org/10.1371/journal.pone.0269449.](https://doi.org/10.1371/journal.pone.0269449)
Partescano, E., et al., 2021. Data quality and FAIR principles applied to marine litter data
[in Europe. Mar. Pollut. Bull. 173, 112965 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2021.112965)
[marpolbul.2021.112965.](https://doi.org/10.1016/j.marpolbul.2021.112965)
Pham, C.K., et al., 2014. Marine litter distribution and density in European Seas, from the
[shelves to deep basins. PLoS One 9 (4), 1831. https://doi.org/10.1371/journal.](https://doi.org/10.1371/journal.pone.0095839)
[pone.0095839 e95839.](https://doi.org/10.1371/journal.pone.0095839)
Pinto, L., Andriolo, U., Goncalves, G., 2021. Detecting stranded macro-litter categories
on drone orthophoto by a multi-class neural network. Mar. Pollut. Bull. 169, 112594
[https://doi.org/10.1016/j.marpolbul.2021.112594.](https://doi.org/10.1016/j.marpolbul.2021.112594)
Politikos, D.V., Fakiris, E., Davvetas, A., Klampanos, I.A., Papatheodorou, G., 2021.
Automatic detection of seafloor marine litter using towed camera images and deep
[learning. Mar. Pollut. Bull. 164, 111974. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2021.111974)
[marpolbul.2021.111974.](https://doi.org/10.1016/j.marpolbul.2021.111974)
Priyadarshini, I., Alkhayyat, A., Obaid, A.J., Sharma, R., 2022. Water pollution reduction
for sustainable urban development using machine learning techniques. Cities 130,
[103970. https://doi.org/10.1016/j.cities.2022.103970.](https://doi.org/10.1016/j.cities.2022.103970)
Proenca, P.F., Simoes, P., 2020. TACO: Trash Annotations in Context for Litter Detection
[arXiv preprint. https://arxiv.org/abs/2003.06975.](https://arxiv.org/abs/2003.06975)
Ramdani, F., Sianturi, R.S., Furqon, M.T., Ananta, M.T., 2022. Mapping riparian zone
macro litter abundance using combination of optical and thermal sensor. Sci. Rep.
[12, 6081. https://doi.org/10.1038/s41598-022-09974-4.](https://doi.org/10.1038/s41598-022-09974-4)
Redmon, J., Divvala, S., Girshick, R., Farhadi, A., 2016. You only look once: unified,
[realtime object detection. arXiv preprint. https://doi.org/10.48550/arXiv.1506.](https://doi.org/10.48550/arXiv.1506.02640)
[02640.](https://doi.org/10.48550/arXiv.1506.02640)

Ronen, M., Finder, S.E., Freifeld, O., 2022. DeepDPM: deep clustering with an unknown
[number of clusters. arXiv preprint. https://doi.org/10.48550/arXiv.2203.14309.](https://doi.org/10.48550/arXiv.2203.14309)


17


-----

_D.V. Politikos et al.                                                                                                               Ocean and Coastal Management 233 (2023) 106466_


Salgado-Hernanz, P.M., et al., 2021. Assessment of marine litter through remote sensing:
[recent approaches and future goals. Mar. Pollut. Bull. 168, 112347 https://doi.org/](https://doi.org/10.1016/j.marpolbul.2021.112347)
Sanchez-Ferrer, A., Gallego, A.J., Valero-Mas, J.J., Calvo-Zaragoza, J., 2022. The ´ [10.1016/j.marpolbul.2021.112347.](https://doi.org/10.1016/j.marpolbul.2021.112347)
CleanSea set: A bbenchmark corpus for underwater debris detection and recognition. In: Pinho, A.J., Georgieva, P., Teixeira, L.F., Sanchez, J.A. (Eds.), Pattern ´
Recognition and Image Analysis. IbPRIA 2022, Lecture Notes in Computer Science,
[13256. Springer, Cham. https://doi.org/10.1007/978-3-031-04881-4_49.](https://doi.org/10.1007/978-3-031-04881-4_49)
Sannigraphi, S., Basu, B., Basu, A.S., Pilla, F., 2022. Development of automated marine
floating plastic detection system using Sentinel-2 imagery and machine learning
[models. Mar. Pollut. Bull. 178, 113527 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2022.113527)
[marpolbul.2022.113527.](https://doi.org/10.1016/j.marpolbul.2022.113527)
Sarker, I.H., 2021. Machine learning: algorithms, real-world applications and research
[directions. SN Comput. Sci. 2, 160. https://doi.org/10.1007/s42979-021-00592-x.](https://doi.org/10.1007/s42979-021-00592-x)
Sasaki, K., et al., 2022. Coastal marine debris detection and density mapping with very
high resolution satellite imagery. IEEE J. Sel. Top. Appl. Earth Obs. Rem. Sens. 15,
[Savastano, S., Cester, I., Perpiny6391–6401. https://doi.org/10.1109/JSTARS.2022.3193993`a, M., Romero, L., 2021. A first approach to the .](https://doi.org/10.1109/JSTARS.2022.3193993)
automatic detection of marine litter in SAR images using artificial intelligence. Int.
[Geosci. Remote Sens. Symp. 8704–8707. https://doi.org/10.1109/](https://doi.org/10.1109/IGARSS47720.2021.9737038)
[IGARSS47720.2021.9737038.](https://doi.org/10.1109/IGARSS47720.2021.9737038)
Schulz, M., Matthies, M., 2014. Artificial neural networks for modeling time series of
[beach litter in the southern North Sea. Mar. Environ. Res. 98, 14–20. https://doi.](https://doi.org/10.1016/j.marenvres.2014.03.014)
[org/10.1016/j.marenvres.2014.03.014.](https://doi.org/10.1016/j.marenvres.2014.03.014)
Shi, B., et al., 2022. Automatic quantification and classification of microplastics in
scanning electron micrographs via deep learning. Sci. Total Environ. 825, 153903
[https://doi.org/10.1016/j.scitotenv.2022.153903.](https://doi.org/10.1016/j.scitotenv.2022.153903)
Simonyan, K., Zisserman, A., 2014. Very deep convolutional networks for large-scale
[image recognition. arXiv preprint. https://doi.org/10.48550/arXiv.1409.1556.](https://doi.org/10.48550/arXiv.1409.1556)
Song, K., Jung, J.-Y., Lee, S.H., Park, S., 2021. A comparative study of deep learningbased network model and conventional method to assess beach debris standing[stock. Mar. Pollut. Bull. 168, 112466 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpolbul.2021.112466)
[marpolbul.2021.112466.](https://doi.org/10.1016/j.marpolbul.2021.112466)
Szegedy, C., et al., 2014. Going deeper with convolutions. In: Proceedings of the 2015
IEEE Conference on Computer Vision and Pattern Recognition (CVPR), USA, pp. 1–9.
[https://doi.org/10.48550/arXiv.1409.4842.](https://doi.org/10.48550/arXiv.1409.4842)
Taddia, Y., Corbau, C., Buoninsegni, J., Simeoni, U., Pellegrinelli, A., 2021. UAV
approach for detecting plastic marine debris on the beach: a case study in the Po
[River Delta (Italy). Drones 5, 140. https://doi.org/10.3390/drones5040140, 2021.](https://doi.org/10.3390/drones5040140)
Taggio, N., et al., 2022. Combination of machine learning algorithms for marine plastic
[litter detection exploiting hyperspectral PRISMA data. Rem. Sens. 14, 3606. https://](https://doi.org/10.3390/rs14153606)
[doi.org/10.3390/rs14153606.](https://doi.org/10.3390/rs14153606)
Takaya, K., Shibata, A., Mizuno, Y., Ise, T., 2022. Unmanned aerial vehicles and deep
learning for assessment of anthropogenic marine debris on beaches on an island in a
[semi-enclosed sea in Japan. Environ. Res. Commun. 4, 015003 https://doi.org/](https://doi.org/10.1088/2515-7620/ac473b)
[10.1088/2515-7620/ac473b.](https://doi.org/10.1088/2515-7620/ac473b)
Tan, M., Pang, R., Le, Q.V., 2020. EfficientDet: scalable and efficient object detection.
[arXiv preprint. https://doi.org/10.48550/arXiv.1911.09070.](https://doi.org/10.48550/arXiv.1911.09070)
Tata, G., 2021. DeepPlastic: an Open Source Image Dataset for Epipelagic Marine Plastic
[Detection. https://zenodo.org/record/5562940#.Y2OyH3ZByUk.](https://zenodo.org/record/5562940#.Y2OyH3ZByUk)
Tata, G., Royer, S.-J., Poirion, O., Lowe, J., 2021. A robotic approach towards
quantifying epipelagic bound plastic using deep visual models. arXiv preprint..
[https://doi.org/10.48550/arXiv.2105.01882.](https://doi.org/10.48550/arXiv.2105.01882)
Teng, C., Kylili, K., Hadjistassou, C., 2022. Deploying deep learning to estimate the
abundance of marine debris from video footage. Mar. Pollut. Bull. 183, 114049
[https://doi.org/10.1016/j.marpolbul.2022.114049.](https://doi.org/10.1016/j.marpolbul.2022.114049)
Tharani, M., Amin, A.W., Maaz, M., Taj, M., 2020. Attention Neural Network for Trash
[Detection on Water Channels, 04639 arXiv:2007. https://arxiv.org/abs/2](https://arxiv.org/abs/2007.04639)
[007.04639.](https://arxiv.org/abs/2007.04639)


Themistocleous, K., Papoutsa, C., Michaelides, S., Hadjimitsis, D., 2020. Investigating
detection of floating plastic litter from space using Sentinel-2 imagery. Rem. Sens.
[12, 2648. https://doi.org/10.3390/rs12162648.](https://doi.org/10.3390/rs12162648)
Thiel, M., et al., 2003. Floating marine debris in coastal waters of the SE-pacific (Chile).
[Mar. Pollut. Bull. 46, 224–231. https://doi.org/10.1016/s0025-326x(02)00365-x.](https://doi.org/10.1016/s0025-326x(02)00365-x)
Topouzelis, K., Papakonstantinou, A., Garaba, S.P., 2019. Detection of floating plastics
from satellite and unmanned aerial systems (plastic litter project 2018). Int. J. Appl.
[Earth Obs. Geoinformation 79, 175–183. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.jag.2019.03.011)
[jag.2019.03.011.](https://doi.org/10.1016/j.jag.2019.03.011)
Topouzelis, K., Papageorgiou, D., Suaria, G., 2021. Floating marine litter detection
algorithms and techniques using optical remote sensing data: a review. Mar. Pollut.
[Bull. 112675 https://doi.org/10.1016/j.marpolbul.2021.112675.](https://doi.org/10.1016/j.marpolbul.2021.112675)
UNEP, 2021. From Pollution to Solution: A Global Assessment of Marine Litter and
[Plastic Pollution. UNEP report UNEA process, p. 148. https://wedocs.unep.org/](https://wedocs.unep.org/bitstream/handle/20.500.11822/36963/POLSOL.pdf)
[bitstream/handle/20.500.11822/36963/POLSOL.pdf.](https://wedocs.unep.org/bitstream/handle/20.500.11822/36963/POLSOL.pdf)
[UNEP/MAP, 2016. In: United (Ed.), Marine Litter Assessment in the Mediterranean 2015.](http://refhub.elsevier.com/S0964-5691(22)00442-2/sref160)
Valdenegro-Toro, M., 2016. Submerged marine debris detection with autonomous
underwater vehicles. In: 2016 International Conference on Robotics and Automation

[for Humanitarian Applications (RAHA), pp. 1–7. https://doi.org/10.1109/](https://doi.org/10.1109/RAHA.2016.7931907)
[RAHA.2016.7931907.](https://doi.org/10.1109/RAHA.2016.7931907)

Van Gansbeke, W., Vandenhende, S., Georgoulis, S., Proesmans, M., Van Gool, L., 2020.
[SCAN: Learning to Classify Images without Labels. https://doi.org/10.48550/](https://doi.org/10.48550/arXiv.2005.12320)
[arXiv.2005.12320 arXiv preprint.](https://doi.org/10.48550/arXiv.2005.12320)
van Lieshout, C., van Oeveren, K., van Emmerik, T., Postma, E., 2020. Automated river
plastic monitoring using deep learning and cameras. Earth Space Sci. 7,
[e2019EA000960 https://doi.org/10.1029/2019EA000960.](https://doi.org/10.1029/2019EA000960)
van Sebille, et al., 2020. The physical oceanography of the transport of floating marine
[debris. Environ. Res. Lett. 15 (2), 023003 https://doi.org/10.1088/1748-9326/](https://doi.org/10.1088/1748-9326/ab6d7d)
[ab6d7d.](https://doi.org/10.1088/1748-9326/ab6d7d)

Veerasingam, S., et al., 2022. Detection and assessment of marine litter in an uninhabited
island, Arabian Gulf: a case study with conventional and machine learning
[approaches. Sci. Total Environ. 838, 156064. https://doi.org/10.1016/j.](https://doi.org/10.1016/j.scitotenv.2022.156064)
[scitotenv.2022.156064.](https://doi.org/10.1016/j.scitotenv.2022.156064)

Vince, J., Hardesty, B., 2018. Governance solutions to the tragedy of the commons that
[marine plastics have become. Front. Mar. Sci. 5, 214. https://doi.org/10.3389/](https://doi.org/10.3389/fmars.2018.00214)
[fmars.2018.00214.](https://doi.org/10.3389/fmars.2018.00214)

Visin, F., et al., 2016. Reseg: a recurrent neural network-based model for semantic
[segmentation. arXiv preprint. https://doi.org/10.48550/arXiv.1511.07053.](https://doi.org/10.48550/arXiv.1511.07053)
Wang, S., 2022. International law-making process of combating plastic pollution: status
[Quo, debates and prospects. Mar. Pol. 147, 105376 https://doi.org/10.1016/j.](https://doi.org/10.1016/j.marpol.2022.105376)
[marpol.2022.105376.](https://doi.org/10.1016/j.marpol.2022.105376)
Wang, Y., et al., 2015. Aquatic debris detection using embedded camera sensors. Sensors
[15, 3116–3137. https://doi.org/10.3390/s150203116.](https://doi.org/10.3390/s150203116)
Watanabe, J., Shao, Y., Miura, N., 2019. Underwater and airborne monitoring of marine
[ecosystems and debris. J. Appl. Remote Sens. 13 (4), 044509 https://doi.org/](https://doi.org/10.1117/1.JRS.13.044509)
[10.1117/1.JRS.13.044509.](https://doi.org/10.1117/1.JRS.13.044509)
Wolf, M., et al., 2020. Machine learning for aquatic plastic litter detection, classification
[and quantification (APLASTIC-Q). Environ. Res. Lett. 15, 114042 https://doi.org/](https://doi.org/10.1088/1748-9326/abbd01)
[10.1088/1748-9326/abbd01.](https://doi.org/10.1088/1748-9326/abbd01)
Xue, B., Huang, B., Chen, G., Li, H., Wei, W., 2021. Deep-sea debris identification using
deep convolutional neural networks. IEEE J. Sel. Top. Appl. Earth Obs. Rem. Sens.
[14, 8909–8921. https://doi.org/10.1109/JSTARS.2021.3107853.](https://doi.org/10.1109/JSTARS.2021.3107853)
Xue, et al., 2021b. An efficient deep-sea debris detection method using deep neural
[networks. IEEE J. Sel. Top. Appl. Earth Obs. Rem. Sens. 14, 12348–12360. https://](https://doi.org/10.1109/JSTARS.2021.3130238)
[doi.org/10.1109/JSTARS.2021.3130238.](https://doi.org/10.1109/JSTARS.2021.3130238)
Zaidi, S.S.A., et al., 2021. A survey of modern deep learning based object detection
[models. arXiv preprint. https://arxiv.org/abs/2104.11892.](https://arxiv.org/abs/2104.11892)
Zbyszewski, M., Corcoran, P.L., Hockin, A., 2014. Comparison of the distribution and
degradation of plastic debris along shorelines of the Great Lakes, North America.
[J. Great Lake. Res. 40 (2), 288–299. https://doi.org/10.1016/j.jglr.2014.02.012.](https://doi.org/10.1016/j.jglr.2014.02.012)


18


-----

