
<img src="https://dataroots.io/rectangle-symbol-rainbow.png" width=74 align="right">
<h1 style="padding-top: 24px">🖖 Welcome to Dataroots' GitHub org</h1>

[![youtube](https://github.com/datarootsio/.github/raw/main/profile/assets/youtube.png)](https://www.youtube.com/c/dataroots)
[![meetup](https://github.com/datarootsio/.github/raw/main/profile/assets/meetup.png)](https://www.meetup.com/rootlabs-x/)
[![web](https://github.com/datarootsio/.github/raw/main/profile/assets/www.png)](https://dataroots.io)
[![blog](https://github.com/datarootsio/.github/raw/main/profile/assets/blogger.png)](https://dataroots.io/research/contributions)
[![hugginface](https://github.com/datarootsio/.github/raw/main/profile/assets/hugginface.png)](https://huggingface.co/dataroots)
[![instagram](https://github.com/datarootsio/.github/raw/main/profile/assets/instagram.png)](https://www.instagram.com/lifeatdataroots/)
[![linkedin](https://github.com/datarootsio/.github/raw/main/profile/assets/linkedin.png)](https://www.linkedin.com/company/dataroots)
[![twitter](https://github.com/datarootsio/.github/raw/main/profile/assets/twitter.png)](https://twitter.com/Datarootsio)
[![email](https://github.com/datarootsio/.github/raw/main/profile/assets/email.png)](mailto:info@dataroots.io)

> Dataroots was founded out of a strong belief that AI & data-driven solutions can be used by companies to gain a competitive edge in terms of company processes, customer interactions and legal compliance. Our mission is to deliver data-driven solutions with unrivalled longevity and business impact for our clients.


ℹ️ Feel free to browse around, below are some quick starting points.

## Terraform

- [terraform-module-azure-datalake](https://github.com/datarootsio/terraform-module-azure-datalake): Terraform module for an Azure Data Lake
- [terraform-module-kubeflow](https://github.com/datarootsio/terraform-module-kubeflow): Kubeflow deployment purely in Terraform
- [terraform-aws-ecs-airflow](https://github.com/datarootsio/terraform-aws-ecs-airflow): A terraform module that creates an airflow instance in AWS ECS
- [terraform-module-kubernetes-application](https://github.com/datarootsio/terraform-module-kubernetes-application): Terraform module for a kubernetes application
- [terraform-provider-kubeflowpipelines](https://github.com/datarootsio/terraform-provider-kubeflowpipelines): Terraform provider for Kubeflow pipelines API
- [terraform-module-azure-storage-sas](https://github.com/datarootsio/terraform-module-azure-storage-sas): Terraform module for Azure Storage SAS tokens
- [terraform-module-azure-snowflake](https://github.com/datarootsio/terraform-module-azure-snowflake): Terraform module for Snowflake on Azure

## Tutorials

- [tutorial-great-expectations](https://github.com/datarootsio/tutorial-great-expectations): A tutorial for the Great Expectations library.
<a href="https://colab.research.google.com/github/datarootsio/tutorial-great-expectations/blob/main/tutorial_great_expectations.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>
- [tutorial-face-mask-detection](https://github.com/datarootsio/tutorial-face-mask-detection): A tutorial to detect masks, using MobileNetV1.
- [tutorial-mlops](https://github.com/datarootsio/tutorial-mlops): A tutorial to learn MLOps best practices with an example using DVC, pycaret and MLflow. <a href="https://colab.research.google.com/github/datarootsio/mlops-workshop/blob/main/notebooks/MLOps_Tutorial.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>, with its exercises <a href="https://colab.research.google.com/github/datarootsio/mlops-workshop/blob/main/notebooks/MLOps_Exercise.ipynb" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>
- [tutorial-hyperparameter-optimization](https://github.com/datarootsio/tutorial-hyperparameter-optimization): A tutorial to know about the latest hyperparameters optimization techniques. <a href="https://colab.research.google.com/drive/1fNzrF96E-Uhexdd0mFITsp-YpWZ2Mzwa" target="_blank" rel="noopener noreferrer"><img src="https://colab.research.google.com/assets/colab-badge.svg"></a>
- [tutorial-streamlit-demo](https://github.com/datarootsio/tutorial-streamlit-demo): A demo of what you can do with streamlit.
- [tutorial-anomalib-demo](https://github.com/datarootsio/anomalib-demo): A demo of what you can do with anomalib to detect anomalies in images.

## Templates

- [ml-skeleton-py](https://github.com/datarootsio/ml-skeleton-py): An opinionated project template that allows you to get started on a new machine learning project.
- [skeleton-pyspark](https://github.com/datarootsio/skeleton-pyspark): An opinionated project template that allows you to get started on an ETL job with PySpark.

## Models

- [face-mask-detection](https://github.com/datarootsio/face-mask-detection): A face mask detection model 😷
- [fresh-coffee-listener](https://github.com/datarootsio/fresh-coffee-listener): Sound detection model to automatically count coffee consumption ☕️
- [snowflake-ml](https://github.com/datarootsio/snowflake-ml): Toy use case on how to use Snowflake as a full ML platform. ❄️

## Rootsacademy Projects:

- [bikefitting](https://github.com/datarootsio/bikefitting): A project to use video of someone biking to get a recommendation on the optimal saddle height
- [terraform-module-azure-snowflake](https://github.com/datarootsio/terraform-module-azure-snowflake): Terraform module for Snowflake on Azure

## Open source packages

- [databooks](https://github.com/datarootsio/databooks): for sharing and caring about Jupyter notebooks ❤️
- [cheek](https://github.com/datarootsio/cheek): Crontab-like scHeduler for Effective Execution of tasKs, cheek for short
- [phonehome](https://github.com/datarootsio/phonehome): KISS telemetry for FOSS packages
- [expiring-lru-cache](https://github.com/datarootsio/expiring-lru-cache): LRU caching with expiration period
- [rootsstyle](https://github.com/datarootsio/rootsstyle): a dataroots inspired style for Matplotlib
- [artyfarty](https://github.com/datarootsio/artyfarty): ggplot2 theme + palette presets

<!-- [[[cog
import os
import cog
from dataroots_profile import eventbrite

cog.out(
    eventbrite.info(key=os.environ["EVENTBRITE_KEY"])
)
]]] -->
## Our events 🍻

Check out all our events at [dataroots.io/events/](https://dataroots.io/events/) or sign up to our [weekly digest](http://eepurl.com/gzXeR5) 👈
<!-- [[[end]]] -->

<!-- [[[cog
import os
import cog
from dataroots_profile import ghost

cog.out(
    ghost.info(key=os.environ["GHOST_KEY"])
)
]]] -->
## Our blog ✍️

Our latest posts:

- [Using Digital Trace Data to Predict Disease Prevalence [COVID-19 Infections] in Belgian Municipalities/ Using Twitter to predict Covid infections in Belgium (02/04/2023)](https://dataroots.io/research/contributions/is-it-possible-to-predict-disease-spread-based-on-digital-trace-data)
- [SOS - RuntimeError: CUDA Out of memory (27/03/2023)](https://dataroots.io/research/contributions/runtimeerror-cuda-out-of-memory)
- [A gentle introduction to blockchain (19/03/2023)](https://dataroots.io/research/contributions/a-gentle-introduction-to-blockchain)
- [Quantitatively measuring speech quality and training a text-to-speech model for Flemish Dutch (05/03/2023)](https://dataroots.io/research/contributions/text-to-speech-in-flemish)
- [Is edge computing just a buzzword? (26/02/2023)](https://dataroots.io/research/contributions/working-on-the-edge)

Check out all our posts at [dataroots.io/research/contributions/](https://dataroots.io/research/contributions/) 👈
<!-- [[[end]]] -->

<!-- [[[cog
import cog
from dataroots_profile import recruitee

cog.out(
    recruitee.info()
)
]]] -->
## Join our team! ❤️

Our open positions:

- [🕹 Tech Lead Data & Cloud](https://careers.dataroots.io/o/tech-lead-data-cloud)
- [🛠 Experienced Data Engineer](https://careers.dataroots.io/o/experienced-data-engineer-hybrid)
- [🛠 Experienced Data Engineer 🇳🇱](https://careers.dataroots.io/o/experienced-data-engineer-maastricht)
- [🛠 Experienced Data Engineer 🇪🇸](https://careers.dataroots.io/o/experienced-data-engineer-malaga-hybrid-remote)
- [🛠 Experienced Analytics Engineer](https://careers.dataroots.io/o/experienced-analytics-engineer)
- [⛅️ Experienced Cloud Engineer](https://careers.dataroots.io/o/experienced-cloud-engineer)
- [🤖  Experienced Machine Learning Engineer](https://careers.dataroots.io/o/experienced-machine-learning-engineer)
- [📊  Data Analyst](https://careers.dataroots.io/o/data-analyst)
- [🤝  Data Strategy Consultant](https://careers.dataroots.io/o/data-strategy-consultant)
- [🤝  Data Governance Expert](https://careers.dataroots.io/o/data-governance-expert-hybrid)
- [🛠 Junior Data Engineer](https://careers.dataroots.io/o/junior-data-engineer-hybrid)
- [🤝Junior Data Strategy Consultant](https://careers.dataroots.io/o/junior-data-strategy-consultant)
- [🤖  Junior Machine Learning Engineer](https://careers.dataroots.io/o/junior-machine-learning-engineer-leuven)

For more info check out [dataroots.io/careers](https://dataroots.io/careers) 👈
<!-- [[[end]]] -->
