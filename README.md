# Yarn Image cross-section Analysis


## Introduction 

Before getting started into the actual project here is an hypothetical situation to understand the world of textile. I will discuss very briefly about shape of fibers and how it affects fiber's physical property. 

## About Fibers and Yarns
As shown in the image below, fibers are used to make yarn, yarns are used to make up fabric.
![img_2.png](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/c378eb4f-34e1-4ada-b8f7-91372a6bf315)

Many physical properties of the fabric like texture, warmth, water-retention, etc. depends on the kind of fibre used in making the yarn and then fabric. Different fibres has different shape and hence different property like, As shown in image, cotton, a natural fibre, tends to have convulated strand which gives it the rough texture, polyester, a man made fiber has circular shape and have smooth and shinny texture.  Images below shows different type of cross-section for different type of fibers.

![img_3.png](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/d107c3e9-7ce0-4d66-9405-e35fc565858f)
 These property also comes from their inherent molecular structure and physical appearance of it. One very prominent example of this is hollow fibers, used in most of the blankets and pillows. The most important property of these fibers is their remarkable thermal insulation property, which is resulted from the air trapped inside the hollow structure and as we know air is a great insulator of heat.  
![img_4.png](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/e578dfb5-ec5b-4650-b380-d1dc59d0b88f)

## About Blended Yarn
Now, lets take a hypothetical problem, we want to design a new kind of fabric, this need to have cotton like texture but should be quick-dry like polyester cloths. How do we go about creating such a fabric? Let me answer, we do this by using a blended yarn. You may ask, what the hack is Blended yarn?  Let me Explain.   
Imagine a yarn like a big circle in which small circular strands of small circle (i.e. fibers) are kept. As shown in image below with grey and black circle. In very crude terms fiber on the outside will decide how the texture of fabric would be, while the fiber on the inside making the bulk would decide its other property. Now, let's come back to our original case, we want texture of cotton, so we would use cotton fibers on outer circle. We want the fabric to also dry-quickly, a property of hydro-phobic polyester fiber, so we will use polyester in the core (i.e Grey circle).  And Eureka!!! our recipe for the hypothetical Fabric is ready!!! Congratulations, on just inventing a first of kind its fabric. Now We will send it for manufacturing.  
<table>
  <tr>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/4957215e-8145-47d5-847f-b0973386d947" alt="Image 5" width="200"></td>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/356ef657-b2fc-4cfd-bb16-fedf2b87ce57" alt="Image 6" width="200"></td>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/411a9cfe-863a-4a6a-94ec-6b3cc30d52f9" alt="Image 7" width="200"></td> 
  </tr>
</table>  

## More Trouble
Small update, manufacturer has told us to go to sheep-yard, he can't manufacture such a yarn. It's not technically and mechanically fissible to create the given distribution of fiber. So we have decided to put our years of textile innovator mind-set into action and take things into our own hand. We directly landed into textile research lab, started our yarn spinning machine, change some parameter and feed supply into this gigantic machine and created a yarn ourselves.  We cut the yarn cross-section, took 10-15 samples put it under microscope and observe what we have created.  Below is what we observed. Now we need to analyze and report density of both fibers. Images-3, Oopsie!! this is not what we desired.   
<table>
  <tr>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/0c0849c1-0526-4345-8107-dc597b300c61" alt="Image 5" width="200"></td>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/84af5e2b-4dda-479e-80e1-29eff5ced609" alt="Image 6" width="200"></td>  
    <td><img src="https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/76037efd-a0a5-425f-bf50-917e8b272b76" alt="Image 7" width="200"></td> 
  </tr>
</table>
Still we went on to see how the density of different fiber is varying when we move radially outwards in concentric circles. polyester-density = (white_area in ring/total_area of ring), based on which we plotted density at different radius values and plotted the graph shown above.  
After a year of hard work and multiple experimentation we have got the exact method by which industry can produce our specially designed yarn.  

![img_13.png](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/b5a3ee56-c6fa-4724-a110-59426182e928)

## Problem Statement 
In the above example, after getting images from microscope, we have to manually mark every pixel with different color for each type of the fiber and then do the radial density analysis manually. To put salt on the wound, we also have to do this process multiple time, for each yarn experiment, to be sure that is in not an anomalous observation. This marking of image and radial density calculation can be easily automated using the Computer-vision techniques.  

# Solution.




# YarnCrossectionImageProcessing

This project has the code for creating a draw board using python on which user can draw some images, which are then saved and used in final training model.

This project uses CNN for training over 10,000 images of yarn cross-section to predict the type of the fiber and the radial density of the fibers along the radius.

This task which has been done manually could be eaisly automated also expeidting the process of analyzing the different yarn type for their different property.

The final result of the algorithm predict with >95% accuracy the type of fiber in a blended yarn.
for a demo go here :
https://www.youtube.com/watch?v=I1HGaojYO10



![img_9](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/0c0849c1-0526-4345-8107-dc597b300c61)
![img_11](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/84af5e2b-4dda-479e-80e1-29eff5ced609)
![img_12](https://github.com/Im-Himanshu/Yarn-Cross-Section-Image-Processing-CNN/assets/16800094/76037efd-a0a5-425f-bf50-917e8b272b76)
