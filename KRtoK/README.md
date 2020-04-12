## AI_Practice > King-Rook vs. King

<a href="https://www.bilibili.com/video/BV1dJ411B7gh" target="_blank">视频链接</a>

<a href="https://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King%29" target="_blank">数据集链接</a>

---

### King-Rook vs. King (兵王问题)

<a href="https://www.bilibili.com/video/BV1dJ411B7gh?p=14" target="_blank">规则介绍</a>

### 实验具体

实验中使用由**台湾大学林智仁教授**开发的 `libsvm` <a href="https://www.csie.ntu.edu.tw/~cjlin/libsvm/" target="_blank">工具包</a>，进行 `SVM` 模型的训练和测试

实验主要是根据工具包的 <a href="https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf" target="_blank">指导</a>进行：

* `Transform data to the format of an SVM package`

* `Conduct simple scaling on the data`

* `Consider the RBF kernel function K(x, y)`

* `Use cross-validation to find the best parameter C and Gamma`

* `Use the best parameter C and Gamma to train the whole training set`

* `Test`
