# Smithsonian Open Access API Proof of Concept

## Roadmap and Features

This section details the current features of this POC and the roadmap for new features.

| Feature Name                                    | Feature Description                                          | Branch                     | Status |
| ----------------------------------------------- | ------------------------------------------------------------ | -------------------------- | ------ |
| [keep_api_key_secret](./keep_api_key_secret.md) | Key Smithsonian Open Access API secret.                      | develop                    | Merged |
| get_category_terms                              | Use Smithsonian Open Access API to fetch an array of terms based term category | feature/get_category_terms |        |
|                                                 |                                                              |                            |        |



## Running

```
conda activate smith
cd smith-api-poc
python main.py
```

## Setup

1. get an APi Key

    [API KEY](https://api.data.gov/signup/)

1. Download and install Anaconda Python

    Follow the offical instructions:

    - [Installation](https://docs.anaconda.com/anaconda/install/)
    - [Installing on Windows](https://docs.anaconda.com/anaconda/install/windows/)
    - [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)

1. Create a new anaconda Environment

    ```
    conda create --name smith python=3.8
    ```

1. Activate Anaconda Environment

    ```
    conda activate smith
    ```

1. Add PIP Requirements

    ```
    cd smith-api-poc
    pip install -r requirements.txt
    ```