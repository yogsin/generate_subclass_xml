# -*- coding: utf-8 -*-  
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib as mpl  
from matplotlib import cm
def draw_bar(labels,quants):  
    width = 0.4  
    ind = np.linspace(0.5,39.5,80)  
    # make a square figure  
    fig = plt.figure(1)  
    ax  = fig.add_subplot(111)  
    # Bar Plot  
    ax.bar(ind-width/2,quants,width,color='green')  
    # Set the ticks on x-axis  
    ax.set_xticks(ind)  
    ax.set_xticklabels(labels)  
    # labels  
    ax.set_xlabel('category')  
    ax.set_ylabel('AP(%)')  
    # title  
    ax.set_title('per-category AP @ IoU=[0.50,0.95]', bbox={'facecolor':'0.8', 'pad':5})  
    plt.grid(True)  
    plt.show()  
    plt.savefig("bar.jpg")  
    plt.close()  
  
labels   = ['person',
'bicycle',
'car',
'motorcycle',
'airplane',
'bus',
'train',
'ruck',
'boat',
'traffic light',
'fire hydrant',
'stop sign',
'parking meter',
'bench',
'bird',
'cat',
'dog',
'horse',
'sheep',
'cow',
'elephant',
'bear',
'zebra',
'giraffe',
'backpack',
'umbrella',
'handbag',
'tie',
'suitcase',
'frisbee',
'skis',
'snowboard',
'sports ball',
'kite',
'baseball bat',
'baseball glove',
'skateboard',
'surfboard',
'tennis racket',
'bottle',
'wine glass',
'cup',
'fork',
'knife',
'spoon',
'bowl',
'banana',
'apple',
'sandwich',
'orange',
'broccoli',
'carrot',
'hot dog',
'pizza',
'donut',
'cake',
'chair',
'couch',
'potted plant',
'bed',
'dining table',
'toilet',
'tv',
'laptop',
'mouse',
'remote',
'keyboard',
'cell phone',
'microwave',
'oven',
'toaster',
'sink',
'refrigerator',
'book',
'clock',
'vase',
'scissors',
'teddy bear',
'hair drier',
'toothbrush']  
  
quants   = [34.3,
16.8,
19.9,
27.5,
42.2,
48.1,
47.6,
21.1,
12.1,
9.1,
43.1,
47.7,
28.7,
13.4,
18.2,
46.7,
39.4,
38.6,
30.2,
29.2,
43.0,
52.9,
47.6,
50.3,
4.7,
19.5,
3.2,
12.5,
12.0,
30.6,
9.0,
16.2,
13.2,
15.4,
12.5,
14.5,
31.5,
16.3,
27.2,
15.9,
17.9,
20.9,
12.9,
3.8,
4.2,
26.0,
11.8,
9.6,
23.0,
19.7,
14.9,
10.5,
18.4,
34.6,
23.9,
20.3,
13.1,
26.9,
14.0,
30.4,
20.5,
41.0,
41.6,
40.2,
34.7,
8.1,
32.7,
17.9,
35.8,
24.7,
17.5,
21.8,
32.4,
3.4,
29.8,
20.1,
14.0,
29.7,
0.0,
9.4]
#plt.bar(range(len(quants)), quants, tick_label=labels)
#plt.show()
idx = np.arange(len(quants))
color = cm.jet(np.array(quants)/max(quants))
fig = plt.figure(figsize=(80, 50), dpi=80)
plt.bar(idx, quants, color=color)
#plt.yticks(idx+0.4,labels)
plt.xticks( np.arange(80), labels, rotation=90, fontsize=45)
plt.yticks(fontsize=45)
plt.ylim(0, 60)
plt.xlim(0, 80)
plt.grid(axis='y')
plt.ylabel('AP(%)',fontsize=55)
plt.xlabel('category',fontsize=55)
plt.title('per-category AP @ IoU=[0.50,0.95]',fontsize=60)
 
#plt.show()
fig.savefig('temp.png', dpi=fig.dpi)
