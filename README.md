# Game Theory and Collective Phenomena
## Toni Domenech's final thesis on the degree of Physics with a Theretical Physics Major. Advisor: Prof. Josep Perelló.

This project is a study of the behaviour of a user in a collective game.

Here you'll find all the work done in the process.
If you're searching for a general analysis and the work done in all the sections you can read the code in Data_Analysis.ipynb.
If you want to dive deeper on how the clustering is done you can go to cluster.ipynb and there you will see whats in the paper and further representations on how much of each class is on each cluster (this part requires a bit of manual feature selection).
If you want to go directly to the functions we've done to develop this project all of them are on the functions_tfg.py script.
The 3 programs above are commented for me and for my understanding. Thats why maybe they aren't as clear as they should be. Any question you can write me at my mail tonidome@gmail.com and I will be pleased to answer. 

## Conclusions
Humans, while playing collectively follow strategies. There are different kind of strategies. Kinder ones, greedy others. We have seen that in Fig 2 showing the value of the bet probabilities of each round of the game. The first round have quite a lot more importance because the disparity there it's when its higher (Fig 3) and this, in general trends will play a significant role (but not determinant) on the rest of the game.


However, following with Fig 3, we can see how the essence of each player gets truncated by what the others do. The fact to see what others are doing influences our next decission. We have seen on the Fig 3 how the inequality would decrease through the game.

For the following conclusions we think the size of our datasets and the simplicity of the game had strongly influenced them. It would be interesting to build a more complex game or maybe to increase the data of this one. 

It's possible to compute a Mutual Information algorithm with this kind of data and it would give us really different values. In fact, as we have seen in Fig 5, once the data has been cleaned it gives use a considerable network. And we strongly think that with the NetworkX package we should have an amount of tools that could bring this study further.

 We indeed can see how the Mutual Information method can be used for clusteritzation and, as we have seen in figure 7 it is possible to abstract some conclusions from the sociodemographics of each player. We are considering here only sex, education and age. We could study in deep here. Obtain more sociodemographical data and increase our accuracy. As said before, the size of our data prevents us from being categorical with this conclusion. Either way, we have achieved some accurated distinctions between the clusters made off the betting strategies.
 
 This distinctions gave more importance to the education than the age. But our sample is unbalanced so with this conclusion we have to say the same that we had said before. We should get a more balanced set.

If you want the databases used for this project mail me at tonidome@gmail.com
