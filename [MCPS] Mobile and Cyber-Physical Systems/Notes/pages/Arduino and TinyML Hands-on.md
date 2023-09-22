The goal of the hands-on was design a small size neural network, able to run in a resource constrained device, then optimize it.
After Design: Train and then Upload to the device.

Train the neural network to: recognize the activity you want to recognize.
Using the division:
* Training set: train network to recognize the gesture
* Validation set: to optimize the network, you use the validation set, adjust some configuration on the neural network to get some results on those
* Test set: use some part of the set to test, **using some new data not already seen or you are cheating**
We will just train the network, as we suppose that Google Efficiently trained it.


Through Chrome, you can pair with a BL device.
We train the system to recognize a gesture by making it record us doing it.
Then when we execute it, we will the what gesture it recognize and will give also a confidence band.
The more samples we give, the better is the training.

