# keyextract_word2vec
#基于Word2Vec的文本关键词抽取方法

  大多数人都是将Word2Vec作为词向量的等价名词，也就是说，纯粹作为一个用来获取词向量的工具，关心模型本身的读者并不多。
可能是因为模型过于简化了，所以大家觉得这样简化的模型肯定很不准确，所以没法用，但它的副产品词向量的质量反而还不错。
没错，如果是作为语言模型来说，Word2Vec实在是太粗糙了。

  但是，为什么要将它作为语言模型来看呢？
抛开语言模型的思维约束，只看模型本身，我们就会发现，Word2Vec的两个模型 —— CBOW和Skip-Gram —— 实际上大有用途，它们从不同角度来描述了周围词与当前词的关系，而很多基本的NLP任务，都是建立在这个关系之上，如关键词抽取、逻辑推理等。

  有心想了解这个系列的读者，有必要了解一下Word2Vec的数学原理。当然，Word2Vec出来已经有好几年了，介绍它的文章数不胜数，这里我推荐peghoty大神的系列博客：
  http://blog.csdn.net/itplus/article/details/37969519
  为了方便读者阅读，我还收集了两个对应的PDF文件：
word2vector中的数学原理详解.pdf   https://spaces.ac.cn/usr/uploads/2017/04/2833204610.pdf

Deep Learning 实战之 word2vec.pdf   https://spaces.ac.cn/usr/uploads/2017/04/146269300.pdf

其中第一个就是推荐的peghoty大神的系列博客的PDF版本。当然，英文好的话，可以直接看Word2Vec的原始论文：
[1] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient Estimation of Word Representations in Vector Space. In Proceedings of Workshop at ICLR, 2013.

[2] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado, and Jeffrey Dean. Distributed Representations of Words and Phrases and their Compositionality. In Proceedings of NIPS, 2013.


简单来说，Word2Vec就是“两个训练方案＋两个提速手段”，所以严格来讲，它有四个备选的模型。两个训练方案分别是CBOW和Skip-Gram。

  用通俗的语言来说，就是“周围词叠加起来预测当前词”（P(W_t|Context)）和“当前词分别来预测周围词”（P(W_others|W_t)），也就是条件概率建模问题了；两个提速手段，分别是层次Softmax和负样本采样。层次Softmax是对Softmax的简化，直接将预测概率的效率从O(|V|)降为O(log2|V|)，但相对来说，精度会比原生的Softmax略差；负样本采样则采用了相反的思路，它把原来的输入和输出联合起来当作输入，然后做一个二分类来打分，这样子我们可以看成是联合概率P(W_t,Context)和P(W_others,W_t)的建模了，正样本就用语料出现过的，负样本就随机抽若干。更多的内容还是去细看peghoty大神的系列博客比较好，我也是从中学习Word2Vec的实现细节的。

  最后，要指出的是，本系列所使用的模型是“Skip-Gram + 层次Softmax”的组合，也就是要用到P(W_others|W_t)这个模型的本身，而不仅仅是词向量。所以，要接着看本系列的读者，需要对Skip-Gram模型有些了解，并且对层次Softmax的构造和实现方式有些印象。
  
  ##1.Word2Vec词向量表示
  
  众所周知，机器学习模型的输入必须是数值型数据，文本无法直接作为模型的输入，需要首先将其转化成数学形式。基于Word2Vec词聚类方法正是一种机器学习方法，需要将候选关键词进行向量化表示，因此要先构建Word2Vec词向量模型，从而抽取出候选关键词的词向量。

  Word2Vec是当时在Google任职的Mikolov等人于2013年发布的一款词向量训练工具，一经发布便在自然语言处理领域得到了广泛的应用。该工具利用浅层神经网络模型自动学习词语在语料库中的出现情况，把词语嵌入到一个高维的空间中，通常在100-500维，在新的高维空间中词语被表示为词向量的形式。与传统的文本表示方式相比，Word2Vec生成的词向量表示，词语之间的语义关系在高维空间中得到了较好的体现，即语义相近的词语在高维空间中的距离更近；同时，使用词向量避免了词语表示的“维度灾难”问题。

  就实际操作而言，特征词向量的抽取是基于已经训练好的词向量模型，词向量模型的训练需要海量的语料才能达到较好的效果，而wiki中文语料是公认的大型中文语料，本文拟从wiki中文语料生成的词向量中抽取本文语料的特征词向量。
  

##2.代码执行步骤如下：

（1）运行get_vector.py读取样本源文件data.txt;

（2）获得源文件的分词文件，即data_result.txt，包括分词、去重、去停用词

（3）运行train_word2vec.py，训练词向量模型，得到data.model以及data.vector

（4）运行www.py，读取测试文本test_data.txt，然后就可以提取出对应的关键词
