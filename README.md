<h1 align="center">Neural Networks to Interpolate Simulation Data at the Parameter Limits</h1>

---
## About This Project
- 👓 Supervised and developed under **Armament Research & Development Establishment, Pashan, Pune 411021, India**
- 🔭 The objective of the project is to determine whether neural networks can assist in analysis and simulation fields
- 🔮 The project aims to create a neural network pipeline to interpolate simulation data
- 🌱 If successful, this project has the potential to significantly reduce the time and compute required for experiment development processes
- 🏗️ Made with 💖 using <img height="16" width="16" src="https://cdn.simpleicons.org/pytorch" style="vertical-align: bottom;"/>

---

## 🛠 Current Implementation

Click [here](https://drive.google.com/file/d/1BHDMZEZtfBrlbOZQ3eBgxldSINg1pQ0v/view?usp=share_link) to view the full report

- **[Multi Layer Perceptron - MLP](LINK)** - A simple MLP neural network is being used to predict the results. MLP [baseline](https://wandb.ai/wrongcolor/HVIS_Baseline?workspace=user-wrongcolor), here Loss: mean_squared_error and root_mean_squared_error.. Hyper-parmeters were tunned to minimize the validation loss.
- **[Impact of Pre-Processing](https://wandb.ai/wrongcolor/HVIS_PreProcessingCheck?workspace=user-wrongcolor)** - Detailed view and logs for checking **impact of pre-processing on loss**. Here, Loss: mean_squared_error and root_mean_squared_error.
- **[Using RTDL library](https://github.com/Yura52/rtdl)** - Propsed in [Revisiting Deep Learning Models for Tabular Data](https://arxiv.org/abs/2106.11959), this library contains 3 basic neural network implementations to start working on top of.
- **[Parameter Domain Reduction and its Imapct](https://wandb.ai/wrongcolor/param_domain?workspace=user-wrongcolor)** - Main purpose of this study is to reduce simulation data overhead. Initially, a reduced parameter domain is used to train and study the models.

<!-- ## 📊 Stats -->

---

<!-- ## 💪 To - Do -->

<!-- - [ ] to do here -->
---