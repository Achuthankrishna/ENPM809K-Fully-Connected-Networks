from builtins import range
import numpy as np
from numpy.random import gamma


def affine_forward(x, w, b):
    """Computes the forward pass for an affine (fully connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    - w: A numpy array of weights, of shape (D, M)
    - b: A numpy array of biases, of shape (M,)

    Returns a tuple of:
    - out: output, of shape (N, M)
    - cache: (x, w, b)
    """
    out = None
    ###########################################################################
    # TODO: Copy over your solution from Assignment 1.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = x.shape[0]
    #We do the forward linear function with f(x)=wx+b
    #print(np.shape(num_train),np.shape(w),np.shape(b))
    m=x.reshape(num_train,-1)
    #print(m)
    out=m.dot(w)+b
    

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """Computes the backward pass for an affine (fully connected) layer.

    Inputs:
    - dout: Upstream derivative, of shape (N, M)
    - cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)
      - b: Biases, of shape (M,)

    Returns a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Copy over your solution from Assignment 1.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #As per previous models, we initiate number of training datasets
    num_train = x.shape[0]
    #print(np.shape(num_train),np.shape(w),np.shape(b))
    #print(np.shape(x),np.shape(w),np.shape(dout))
    #First we multiply Upstream gradient with local gradient which is wx+b
    dx=dout.dot(w.T)
    #print(np.shape(dx)) is (10,6)
    #print(np.shape(x))
    #We need to bring dx back into shape of X to find rel error 
    dx=dx.reshape(x.shape)
    #print(np.shape(dx))
    #X is of shape MxNxO and dout MxC , which is impossible to perform the second pass
    #We need to have a Matrix that matches the dimension, so we reshape x along the row.
    #We need to have M along the row to perform function multiplication backward gate
    m=x.reshape(num_train,w.shape[0])
    #dw=x*local gradient -> multiply gate
    dw=m.T.dot(dout)
    #db= dout -> add gate
    db=np.sum(dout)


    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def relu_forward(x):
    """Computes the forward pass for a layer of rectified linear units (ReLUs).

    Input:
    - x: Inputs, of any shape

    Returns a tuple of:
    - out: Output, of the same shape as x
    - cache: x
    """
    out = None
    ###########################################################################
    # TODO: Copy over your solution from Assignment 1.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Taking ReLu function which is max(0,x), for any value of x
    out=np.maximum(0,x)

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = x
    return out, cache


def relu_backward(dout, cache):
    """Computes the backward pass for a layer of rectified linear units (ReLUs).

    Input:
    - dout: Upstream derivatives, of any shape
    - cache: Input x, of same shape as dout

    Returns:
    - dx: Gradient with respect to x
    """
    dx, x = None, cache
    ###########################################################################
    # TODO: Copy over your solution from Assignment 1.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Giving values for only positive values of X as per reLU function, which is max(0,x)
    dx=dout.copy()
    dx[x<0]=0


    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def softmax_loss(x, y):
    """Computes the loss and gradient for softmax classification.

    Inputs:
    - x: Input data, of shape (N, C) where x[i, j] is the score for the jth
      class for the ith input.
    - y: Vector of labels, of shape (N,) where y[i] is the label for x[i] and
      0 <= y[i] < C

    Returns a tuple of:
    - loss: Scalar giving the loss
    - dx: Gradient of the loss with respect to x
    """
    loss, dx = None, None

    ###########################################################################
    # TODO: Copy over your solution from Assignment 1.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = x.shape[0]
    #We define xm as diference of x and max of x to prevent overflow
    xm=x-np.max(x,axis=1,keepdims=True)
    scores = np.exp(xm)
    #Softmax f= e^xy /sum(e^xj)
    prb = scores/np.sum(scores,axis=1,keepdims=True)
    #print(np.shape(prb))
    #We calculate loss for all right labels from the training data set
    #Since we don't know the incorrect data, we directly take with the right data
    #and proceed to find the loss 
    loss=np.sum(-np.log(prb[np.arange(num_train), y]))
    loss/=num_train
    #print(loss) 
    #Gradient differentiation for where j=y is (-1+prb)
    dx=prb.copy()
    #Subtract 1 for all right value
    dx[np.arange(num_train), y] -=1
    #print(prb)
    #We take the mean of the loss as we want to get an average over all training samples   
    dx /= num_train
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return loss, dx


def batchnorm_forward(x, gamma, beta, bn_param):
    """Forward pass for batch normalization.

    During training the sample mean and (uncorrected) sample variance are
    computed from minibatch statistics and used to normalize the incoming data.
    During training we also keep an exponentially decaying running mean of the
    mean and variance of each feature, and these averages are used to normalize
    data at test-time.

    At each timestep we update the running averages for mean and variance using
    an exponential decay based on the momentum parameter:

    running_mean = momentum * running_mean + (1 - momentum) * sample_mean
    running_var = momentum * running_var + (1 - momentum) * sample_var

    Note that the batch normalization paper suggests a different test-time
    behavior: they compute sample mean and variance for each feature using a
    large number of training images rather than using a running average. For
    this implementation we have chosen to use running averages instead since
    they do not require an additional estimation step; the torch7
    implementation of batch normalization also uses running averages.

    Input:
    - x: Data of shape (N, D)
    - gamma: Scale parameter of shape (D,)
    - beta: Shift paremeter of shape (D,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: of shape (N, D)
    - cache: A tuple of values needed in the backward pass
    """
    mode = bn_param["mode"]
    eps = bn_param.get("eps", 1e-5)
    momentum = bn_param.get("momentum", 0.9)

    N, D = x.shape
    running_mean = bn_param.get("running_mean", np.zeros(D, dtype=x.dtype))
    running_var = bn_param.get("running_var", np.zeros(D, dtype=x.dtype))

    out, cache = None, None
    if mode == "train":
        #######################################################################
        # TODO: Implement the training-time forward pass for batch norm.      #
        # Use minibatch statistics to compute the mean and variance, use      #
        # these statistics to normalize the incoming data, and scale and      #
        # shift the normalized data using gamma and beta.                     #
        #                                                                     #
        # You should store the output in the variable out. Any intermediates  #
        # that you need for the backward pass should be stored in the cache   #
        # variable.                                                           #
        #                                                                     #
        # You should also use your computed sample mean and variance together #
        # with the momentum variable to update the running mean and running   #
        # variance, storing your result in the running_mean and running_var   #
        # variables.                                                          #
        #                                                                     #
        # Note that though you should be keeping track of the running         #
        # variance, you should normalize the data based on the standard       #
        # deviation (square root of variance) instead!                        #
        # Referencing the original paper (https://arxiv.org/abs/1502.03167)   #
        # might prove to be helpful.                                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #To perform batchform forward we use the normalized version x-mean(x)/sqrt(var**2+eps)
        #Post normalization we calcualte the transformation out using gamma and beta
        xm=np.mean(x,axis=0)
        #Calculate Variance as a single vector of X
        xv=np.var(x,axis=0)
        mean=x-xm
        std=np.sqrt(xv+eps)
        invertstd=1./std
        #Normalized form is calculated as the ratio of difference of x and its mean and root of variance square
        xhat=(x-xm)/std
        #We use the normalized version to scale and shift 
        scalex=gamma*xhat
        out=(gamma*xhat)+beta
        #Saving the values to the cache and performing running mean along with running variance 
        running_mean = momentum * running_mean + (1 - momentum) * xm
        running_var = momentum * running_var + (1 - momentum) * xv
        cache = (mean,std,x,gamma,beta,eps,xhat,xv,scalex,xm,invertstd)
        pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == "test":
        #######################################################################
        # TODO: Implement the test-time forward pass for batch normalization. #
        # Use the running mean and variance to normalize the incoming data,   #
        # then scale and shift the normalized data using gamma and beta.      #
        # Store the result in the out variable.                               #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        xhat=(x-running_mean)/np.sqrt(running_var+eps)
        out=(gamma*xhat)+beta
        pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    else:
        raise ValueError('Invalid forward batchnorm mode "%s"' % mode)

    # Store the updated running means back into bn_param
    bn_param["running_mean"] = running_mean
    bn_param["running_var"] = running_var

    return out, cache


def batchnorm_backward(dout, cache):
    """Backward pass for batch normalization.

    For this implementation, you should write out a computation graph for
    batch normalization on paper and propagate gradients backward through
    intermediate nodes.

    Inputs:
    - dout: Upstream derivatives, of shape (N, D)
    - cache: Variable of intermediates from batchnorm_forward.

    Returns a tuple of:
    - dx: Gradient with respect to inputs x, of shape (N, D)
    - dgamma: Gradient with respect to scale parameter gamma, of shape (D,)
    - dbeta: Gradient with respect to shift parameter beta, of shape (D,)
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    # Referencing the original paper (https://arxiv.org/abs/1502.03167)       #
    # might prove to be helpful.                                              #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #To initiate backward norm, we start with the cache values stores during th forward pass 
    #Provide dimensionality of the input
    (mean,std,x,gamma,beta,eps,xhat,xv,scalex,xm,invertstd)=cache 
    N, D = dout.shape 
    #Calculate the gradient of last layer 
    dbeta = np.sum(dout, axis=0)
    #Init dscalx as dout for simplification
    dscalx = dout
    #calculating dgamma wrt dl/dgamma= dl/dy*dy/dgamma
    dgamma = np.sum(xhat * dscalx, axis=0)
    #Caculating dbeta wrt dl/db
    dxhat = gamma * dscalx
    #We have a series of operations to perfrom
    #Now xhat we know is x-xm/sqrt(var+eps), we perfrom a mul gate on these two as these are branches
    dinvertstd = np.sum(mean * dxhat, axis=0)
    #calculate gradient wrt 1/sqrt(v+eps)
    ddev_from_mean = invertstd * dxhat
    # 1/x gate for 1/sqrt(v+eps) = dl/dv*dv/dx
    #dl/dv is previous gate result 
    dstdv = -1/(std**2) * dinvertstd
    #Calculating square root gate now - dl/dsq * dsq/dx
    dvar = (0.5) * 1/np.sqrt(xv + eps) * dstdv
    #Moving to numerator x-xm gate for summation dl/dmu=dl/db*db/dmu
    #The variance of mean is 1/N
    ddev_meansq = 1/N * np.ones((N,D)) * dvar
    #square gate for (x-xm)^2
    ddev_from_mean += 2 * mean * ddev_meansq
    #gradient for x-xm and summation of x is 
    dx = 1 * ddev_from_mean
    dmean = -1 * np.sum(ddev_from_mean, axis=0)
    #dl/dx=dl/ds*ds/dx for summation of x features
    dx += 1./N * np.ones((N,D)) * dmean
    pass
  # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def batchnorm_backward_alt(dout, cache):
    """Alternative backward pass for batch normalization.

    For this implementation you should work out the derivatives for the batch
    normalizaton backward pass on paper and simplify as much as possible. You
    should be able to derive a simple expression for the backward pass.
    See the jupyter notebook for more hints.

    Note: This implementation should expect to receive the same cache variable
    as batchnorm_backward, but might not use all of the values in the cache.

    Inputs / outputs: Same as batchnorm_backward
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for batch normalization. Store the    #
    # results in the dx, dgamma, and dbeta variables.                         #
    #                                                                         #
    # After computing the gradient with respect to the centered inputs, you   #
    # should be able to compute gradients with respect to the inputs in a     #
    # single statement; our implementation fits on a single 80-character line.#
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Let dyi/dxi be out final output in forward pass and dout in gradient
    (mean,std,x,gamma,beta,eps,xhat,xv,scalex,xm,invertstd)=cache 
    N = x.shape[0]
    #differentiate dout wrt Dbeta
    dbeta = np.sum(dout, axis=0)
    #Dl/dgamma= dl/dx*dx/dgamma=dout*xhat
    dgamma = np.sum((x - mean) * (xv + eps)**(-1. / 2.) * dout, axis=0)
    #Dl/dx=dl/dxcap*dxcap/dx
    #Applying chain rule on the Xhat equation and differentiating wrt t we get
    #Diff for mean can be written as dmu/dx
    dmea = 1/N * np.sum(dout, axis=0)
    #Diff for variace can be written as dv/dx
    dvar = 2/N * np.sum(mean * dout, axis=0)
    dstd = dvar/(2 * std)
    #Hence dl/dx= dl/dy*dy/dx
    dx = gamma*((dout - dmea)*std - dstd*(mean))/std**2 
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def layernorm_forward(x, gamma, beta, ln_param):
    """Forward pass for layer normalization.

    During both training and test-time, the incoming data is normalized per data-point,
    before being scaled by gamma and beta parameters identical to that of batch normalization.

    Note that in contrast to batch normalization, the behavior during train and test-time for
    layer normalization are identical, and we do not need to keep track of running averages
    of any sort.

    Input:
    - x: Data of shape (N, D)
    - gamma: Scale parameter of shape (D,)
    - beta: Shift paremeter of shape (D,)
    - ln_param: Dictionary with the following keys:
        - eps: Constant for numeric stability

    Returns a tuple of:
    - out: of shape (N, D)
    - cache: A tuple of values needed in the backward pass
    """
    out, cache = None, None
    eps = ln_param.get("eps", 1e-5)
    ###########################################################################
    # TODO: Implement the training-time forward pass for layer norm.          #
    # Normalize the incoming data, and scale and  shift the normalized data   #
    #  using gamma and beta.                                                  #
    # HINT: this can be done by slightly modifying your training-time         #
    # implementation of  batch normalization, and inserting a line or two of  #
    # well-placed code. In particular, can you think of any matrix            #
    # transformations you could perform, that would enable you to copy over   #
    # the batch norm code and leave it almost unchanged?                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #For layer norm performs feautre distinction on one single vector
    #Hence we can perfrom a simple matrix transformation to allow norm to read input as single vector at a time
    xm=np.mean(x,axis=1)
    #Calculate Variance as a single vector of X
    xv=np.var(x,axis=1)
    mean=x.T-xm
    std=np.sqrt(xv+eps)
    invertstd=1./std
    #Normalized form is calculated as the ratio of difference of x and its mean and root of variance square
    xhat=(x.T-xm)/(std)
    #We use the normalized version to scale and shift 
    #scalex=gamma*xhat
    out=(gamma*xhat.T)+beta
    #Saving the values to the cache and performing running mean along with running variance 
    cache = (mean,std,x,gamma,beta,eps,xhat,xv,xm,invertstd)
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return out, cache


def layernorm_backward(dout, cache):
    """Backward pass for layer normalization.

    For this implementation, you can heavily rely on the work you've done already
    for batch normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, D)
    - cache: Variable of intermediates from layernorm_forward.

    Returns a tuple of:
    - dx: Gradient with respect to inputs x, of shape (N, D)
    - dgamma: Gradient with respect to scale parameter gamma, of shape (D,)
    - dbeta: Gradient with respect to shift parameter beta, of shape (D,)
    """
    dx, dgamma, dbeta = None, None, None
    ###########################################################################
    # TODO: Implement the backward pass for layer norm.                       #
    #                                                                         #
    # HINT: this can be done by slightly modifying your training-time         #
    # implementation of batch normalization. The hints to the forward pass    #
    # still apply!                                                            #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #To initiate backward norm, we start with the cache values stores during th forward pass 
    #Provide dimensionality of the input
    (mean,std,x,gamma,beta,eps,xhat,xv,xm,invertstd)=cache
    #Calculate the gradient of last layer 
    dbeta = np.sum(dout, axis=0)
    #Init dscalx as dout for simplification
    dscalx = dout
    #calculating dgamma wrt dl/dgamma= dl/dy*dy/dgamma
    dgamma = np.sum(xhat.T* dscalx, axis=0)
    #Caculating dbeta wrt dl/db
    dxhat = (gamma * dscalx)
    dxhat=np.transpose(dxhat,(1,0))
    N,D= xhat.shape
    dout=dout.T
    #We have a series of operations to perfrom
    #Now xhat we know is x-xm/sqrt(var+eps), we perfrom a mul gate on these two as these are branches
    dinvertstd = np.sum(mean * dxhat, axis=0)
    #calculate gradient wrt 1/sqrt(v+eps)
    ddev_from_mean = invertstd * dxhat
    # 1/x gate for 1/sqrt(v+eps) = dl/dv*dv/dx
    #dl/dv is previous gate result 
    dstdv = -1/(std**2) * dinvertstd
    #Calculating square root gate now - dl/dsq * dsq/dx
    dvar = (0.5) * 1/np.sqrt(xv + eps) * dstdv
    #Moving to numerator x-xm gate for summation dl/dmu=dl/db*db/dmu
    #The variance of mean is 1/N
    ddev_meansq = 1/N * np.ones((N,D)) * dvar
    #square gate for (x-xm)^2
    ddev_from_mean += 2 * mean * ddev_meansq
    #gradient for x-xm and summation of x is 
    dx = 1 * ddev_from_mean
    dmean = -1 * np.sum(ddev_from_mean, axis=0)
    #dl/dx=dl/ds*ds/dx for summation of x features
    dx += 1./N * np.ones((N,D)) * dmean
    dx=dx.T

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dgamma, dbeta


def dropout_forward(x, dropout_param):
    """Forward pass for inverted dropout.

    Note that this is different from the vanilla version of dropout.
    Here, p is the probability of keeping a neuron output, as opposed to
    the probability of dropping a neuron output.
    See http://cs231n.github.io/neural-networks-2/#reg for more details.

    Inputs:
    - x: Input data, of any shape
    - dropout_param: A dictionary with the following keys:
      - p: Dropout parameter. We keep each neuron output with probability p.
      - mode: 'test' or 'train'. If the mode is train, then perform dropout;
        if the mode is test, then just return the input.
      - seed: Seed for the random number generator. Passing seed makes this
        function deterministic, which is needed for gradient checking but not
        in real networks.

    Outputs:
    - out: Array of the same shape as x.
    - cache: tuple (dropout_param, mask). In training mode, mask is the dropout
      mask that was used to multiply the input; in test mode, mask is None.
    """
    p, mode = dropout_param["p"], dropout_param["mode"]
    if "seed" in dropout_param:
        np.random.seed(dropout_param["seed"])

    mask = None
    out = None

    if mode == "train":
        #######################################################################
        # TODO: Implement training phase forward pass for inverted dropout.   #
        # Store the dropout mask in the mask variable.                        #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #Dropout regularization technique invovles zeroing out half of the H1 output
        #The probability of dropping any hyper param is 0.5
        #During training, we create a U layer (mask) which zeroes out half of the size of input
        mask=(np.random.rand(*x.shape)<p)
        #Multiply the mask layer with input to zero out all the values 
        out=x*mask


        pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                           END OF YOUR CODE                          #
        #######################################################################
    elif mode == "test":
        #######################################################################
        # TODO: Implement the test phase forward pass for inverted dropout.   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #During testing, the same method of train won't work for this method. 
        #instead, we need to make the expected output of test same as train
        out=x

        pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                            END OF YOUR CODE                         #
        #######################################################################

    cache = (dropout_param, mask)
    out = out.astype(x.dtype, copy=False)

    return out, cache


def dropout_backward(dout, cache):
    """Backward pass for inverted dropout.

    Inputs:
    - dout: Upstream derivatives, of any shape
    - cache: (dropout_param, mask) from dropout_forward.
    """
    dropout_param, mask = cache
    mode = dropout_param["mode"]

    dx = None
    if mode == "train":
        #######################################################################
        # TODO: Implement training phase backward pass for inverted dropout   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #After loading the cache, we perform a simple backprop function. We know that dl/dy=out and 
        #previous layer is a multiplier gate with mask layer. Perfroming differentiation with this we get
        dx= mask*dout

        pass

        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        #######################################################################
        #                          END OF YOUR CODE                           #
        #######################################################################
    elif mode == "test":
        dx = dout
    return dx


def conv_forward_naive(x, w, b, conv_param):
    """A naive implementation of the forward pass for a convolutional layer.

    The input consists of N data points, each with C channels, height H and
    width W. We convolve each input with F different filters, where each filter
    spans all C channels and has height HH and width WW.

    Input:
    - x: Input data of shape (N, C, H, W)
    - w: Filter weights of shape (F, C, HH, WW)
    - b: Biases, of shape (F,)
    - conv_param: A dictionary with the following keys:
      - 'stride': The number of pixels between adjacent receptive fields in the
        horizontal and vertical directions.
      - 'pad': The number of pixels that will be used to zero-pad the input.

    During padding, 'pad' zeros should be placed symmetrically (i.e equally on both sides)
    along the height and width axes of the input. Be careful not to modfiy the original
    input x directly.

    Returns a tuple of:
    - out: Output data, of shape (N, F, H', W') where H' and W' are given by
      H' = 1 + (H + 2 * pad - HH) / stride
      W' = 1 + (W + 2 * pad - WW) / stride
    - cache: (x, w, b, conv_param)
    """
    out = None
    ###########################################################################
    # TODO: Implement the convolutional forward pass.                         #
    # Hint: you can use the function np.pad for padding.                      #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Our input image is given in the dimensional form of HxWxRGB 
    #Initializing the input and filters
    N,C,H,W=x.shape
    F,C,HH,WW=w.shape
    #Let HHxWW be dimension of filter layer
    S,P=conv_param['stride'],conv_param['pad']
    #We now find the size of output volume is (H-F+2P)/(S)+1
    outp=((H-HH+(2*P))/(S))+1
    outw=((W-WW+(2*P))/S)+1
    #We need create output volume tensor after the convolution of layers
    outp=int(outp)
    outw=int(outw)
    out = np.zeros((N, F, outp, outw))
    #For padding , we create an array to store our input with zero padding applied
    XP=np.zeros((N, C, H+2*P, W+2*P))
    #We need to do padding for input x 
    for i in range(x.shape[0]):
      for j in range(x.shape[1]):
        XP[i][j]=np.pad(x[i][j],P)
    #print(XP.shape)
    #Forward pass of the convolution layer over N neurons and F filters 
    for n in range (N):
      for f in range(F):
        for i in range(outp):
          for j in range(outw):
            #A neuron located in row i, column j of a given layer is connected to the outputs of the neurons in the
            #previous layer located in rows i to i + f h – 1, columns j to j + f w – 1
            out[n,f,i,j]+=np.sum(w[f,...]*XP[n,:,S*i: S*i + HH, S*j: S*j + WW])+b[f]
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, w, b, conv_param)
    return out, cache


def conv_backward_naive(dout, cache):
    """A naive implementation of the backward pass for a convolutional layer.

    Inputs:
    - dout: Upstream derivatives.
    - cache: A tuple of (x, w, b, conv_param) as in conv_forward_naive

    Returns a tuple of:
    - dx: Gradient with respect to x
    - dw: Gradient with respect to w
    - db: Gradient with respect to b
    """
    dx, dw, db = None, None, None
    ###########################################################################
    # TODO: Implement the convolutional backward pass.                        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #initialising x,w,b and dx,dw,db along with cache memory of forward pass
    (x, w, b, conv_param) = cache
    N, C, H, W = x.shape
    F, C, HH, WW = w.shape
    S, P = conv_param['stride'], conv_param['pad']
    outp=((H-HH+(2*P))/(S))+1
    outw=((W-WW+(2*P))/S)+1
    outp=int(outp)
    outw=int(outw)
    out = np.zeros((N, F, outp, outw))
    #For padding , we create an array to store our input with zero padding applied
    XP=np.zeros((N, C, H+2*P, W+2*P))
    #We need to do padding for input x 
    for i in range(x.shape[0]):
      for j in range(x.shape[1]):
        XP[i][j]=np.pad(x[i][j],P)
    #initializing dw as a zero vector
    db=np.zeros_like(b)
    #DX is our input with H and W and N neurons and C Channels 
    dw=np.zeros_like(w)
    dXP=np.zeros_like(XP)
    #For N neurons F filters and the len and b of channels we calculate gradient
    for n in range(N):
      for f in range(F):
        db[f]+=np.sum(dout[n,f,:,:])
        #Dl/dw=dl/dy *dy/dw where dl/dy is out and dy/dw = x[i-a',y-b'][Ref:NPTEL]
        for i in range(outp):
          for j in range(outw):
            dw[f,...]+=XP[n,:,S*i: S*i + HH, S*j: S*j + WW]*dout[n,f,i,j]
            #Now dl/dx=dl/dy*dy/dx where dy/dx=w[a,b]
            dXP[n,:,S*i: S*i + HH, S*j: S*j + WW]+=w[f,...]*dout[n,f,i,j]
    #Since we get out output in terms of padded gradient, we calculate input gradient without pads
    dx=dXP[:,:,P:P+H,P:P+W]      
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dw, db


def max_pool_forward_naive(x, pool_param):
    """A naive implementation of the forward pass for a max-pooling layer.

    Inputs:
    - x: Input data, of shape (N, C, H, W)
    - pool_param: dictionary with the following keys:
      - 'pool_height': The height of each pooling region
      - 'pool_width': The width of each pooling region
      - 'stride': The distance between adjacent pooling regions

    No padding is necessary here, eg you can assume:
      - (H - pool_height) % stride == 0
      - (W - pool_width) % stride == 0

    Returns a tuple of:
    - out: Output data, of shape (N, C, H', W') where H' and W' are given by
      H' = 1 + (H - pool_height) / stride
      W' = 1 + (W - pool_width) / stride
    - cache: (x, pool_param)
    """
    out = None
    ###########################################################################
    # TODO: Implement the max-pooling forward pass                            #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Maxpooling is a layer for making larger convolution layer smaller.
    #It takes the maximum value of the filter for each stride and pass it on to the next Conv
    #We initialize the N C F and H along with W first
    N, C, H, W = x.shape
    PW,PH,S=pool_param['pool_width'],pool_param['pool_height'],pool_param['stride']
    #Finding output of one pool pass
    phout=((H-PH)/S)+1
    pwout=((W-PW)/S)+1
    phout=int(phout)
    pwout=int(pwout)
    out = np.zeros((N, C, phout, pwout))
    for n in range (N):
      for c in range(C):
        for i in range(phout):
          for j in range(pwout):
            #A neuron located in row i, column j of a given layer is connected to the outputs of the neurons in the
            #previous layer located in rows i to i + f h – 1, columns j to j + f w – 1
            #In MAXPOOL layer we take the maximum value of the conv layer 
            #print(x[n,:,S*i: S*i + PH, S*j: S*j + PW])
            #We take the maximum element along the column and row axes
            out[n,:,i,j]=np.max(x[n,:,S*i: S*i + PH, S*j: S*j + PW], axis=(-1,-2))
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    cache = (x, pool_param)
    return out, cache


def max_pool_backward_naive(dout, cache):
    """A naive implementation of the backward pass for a max-pooling layer.

    Inputs:
    - dout: Upstream derivatives
    - cache: A tuple of (x, pool_param) as in the forward pass.

    Returns:
    - dx: Gradient with respect to x
    """
    dx = None
    ###########################################################################
    # TODO: Implement the max-pooling backward pass                           #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #Similar to conv layer, we intialise the cache and other input params
    (x, pool_param)=cache
    N, C, H, W = x.shape
    PW,PH,S=pool_param['pool_width'],pool_param['pool_height'],pool_param['stride']
    #Finding output of one pool pass
    phout=((H-PH)/S)+1
    pwout=((W-PW)/S)+1
    phout=int(phout)
    pwout=int(pwout)
    #initiate dx as an empty zero vector
    dx=np.zeros_like(x)
    #For N neruons, C channels and H XW of the image, we calculate back prop of layer
    for n in range(N):
      for c in range(C):
         for i in range(phout):
            for j in range(pwout):
              #Dl/dx=dl/dy *dy/dx. The derivative of dy/dx is different from zero only if x 
              #is the maximum element in the first pooling operation with respect to the first region.
              #Since we are doing indice wise operation ,initialize ind amnd ind1              
              index = np.argmax(x[n, c, i*S:i*S+PH, j*S:j*S+PW])
              #After getting the max value, we need to compare the maximum value to each index and assign it as 1.
              # the rest all elements becomes zero of the filter and dy/dx =1 for the maximum element
              # we then assign these index values as coordinates using unravel function
              indexa, indexb = np.unravel_index(index,(PH, PW))
              #print(index)
              #print(np.unravel_index(index, (PH, PW)))
              dx[n, c, i*S:i*S+PH, j*S:j*S+PW][indexa,indexb] = dout[n, c, i, j]   
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx


def spatial_batchnorm_forward(x, gamma, beta, bn_param):
    """Computes the forward pass for spatial batch normalization.

    Inputs:
    - x: Input data of shape (N, C, H, W)
    - gamma: Scale parameter, of shape (C,)
    - beta: Shift parameter, of shape (C,)
    - bn_param: Dictionary with the following keys:
      - mode: 'train' or 'test'; required
      - eps: Constant for numeric stability
      - momentum: Constant for running mean / variance. momentum=0 means that
        old information is discarded completely at every time step, while
        momentum=1 means that new information is never incorporated. The
        default of momentum=0.9 should work well in most situations.
      - running_mean: Array of shape (D,) giving running mean of features
      - running_var Array of shape (D,) giving running variance of features

    Returns a tuple of:
    - out: Output data, of shape (N, C, H, W)
    - cache: Values needed for the backward pass
    """
    out, cache = None, None

    ###########################################################################
    # TODO: Implement the forward pass for spatial batch normalization.       #
    #                                                                         #
    # HINT: You can implement spatial batch normalization by calling the      #
    # vanilla version of batch normalization you implemented above.           #
    # Your implementation should be very short; ours is less than five lines. #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #We need to give inputs of our input image 
    N,C,H,W=x.shape
    #for spatial norm, we need to transpose the x and reshape it as a 2D input by multiplying N*H*W
    x = x.reshape(N*H*W,C)
    #perfroming batchnorm to the above mentioned reshaped x
    out, cache = batchnorm_forward(x, gamma, beta, bn_param)
    #getting the output back in 3D form we reshape again to N C H W
    out = out.reshape(N, C, H, W)

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return out, cache


def spatial_batchnorm_backward(dout, cache):
    """Computes the backward pass for spatial batch normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, C, H, W)
    - cache: Values from the forward pass

    Returns a tuple of:
    - dx: Gradient with respect to inputs, of shape (N, C, H, W)
    - dgamma: Gradient with respect to scale parameter, of shape (C,)
    - dbeta: Gradient with respect to shift parameter, of shape (C,)
    """
    dx, dgamma, dbeta = None, None, None

    ###########################################################################
    # TODO: Implement the backward pass for spatial batch normalization.      #
    #                                                                         #
    # HINT: You can implement spatial batch normalization by calling the      #
    # vanilla version of batch normalization you implemented above.           #
    # Your implementation should be very short; ours is less than five lines. #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #We need to give inputs of our input image 
    N,C,H,W=dout.shape
    #for spatial back norm, we need to transpose the dout and reshape it as a 2D input by multiplying N*H*W
    dout = dout.reshape(N*H*W,C)
    #perfroming batchnorm to the above mentioned reshaped x
    dx,dgamma,dbeta = batchnorm_backward(dout,cache)
    #getting the output gradient back in 3D form we reshape again to N C H W
    dx = dx.reshape(N, C, H, W)
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return dx, dgamma, dbeta


def spatial_groupnorm_forward(x, gamma, beta, G, gn_param):
    """Computes the forward pass for spatial group normalization.
    
    In contrast to layer normalization, group normalization splits each entry in the data into G
    contiguous pieces, which it then normalizes independently. Per-feature shifting and scaling
    are then applied to the data, in a manner identical to that of batch normalization and layer
    normalization.

    Inputs:
    - x: Input data of shape (N, C, H, W)
    - gamma: Scale parameter, of shape (1, C, 1, 1)
    - beta: Shift parameter, of shape (1, C, 1, 1)
    - G: Integer mumber of groups to split into, should be a divisor of C
    - gn_param: Dictionary with the following keys:
      - eps: Constant for numeric stability

    Returns a tuple of:
    - out: Output data, of shape (N, C, H, W)
    - cache: Values needed for the backward pass
    """
    out, cache = None, None
    eps = gn_param.get("eps", 1e-5)
    ###########################################################################
    # TODO: Implement the forward pass for spatial group normalization.       #
    # This will be extremely similar to the layer norm implementation.        #
    # In particular, think about how you could transform the matrix so that   #
    # the bulk of the code is similar to both train-time batch normalization  #
    # and layer normalization!                                                #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #As per Author [3] , spatial group norm is similar to batch norm with separated into G groups
    #passing the required inputs of the image before doing batchnorm
    N,C,H,W=x.shape
    #as per author [3], size of the batch is given as 
    size=(N*G,C//G*H*W)
    x1=x.reshape(size).T
    #Now performing batchnorm forward operation
    mean = np.mean(x1,0) #Getting mean of x1 
    var = np.var(x1,0) + eps #calculating variance of x1 and adding eps
    ddm=x1-mean
    #Standard deviation = sqrt(variance)
    std = np.sqrt(var)
    #Normalized form is calculated as the ratio of difference of x and its mean and root of variance square
    xhat = (x1 - mean)/std
    #Bringing back X1 to original dimensions
    x1=x1.T.reshape(N, C, H, W)
    #We use the normalized version to scale and shift 
    out = gamma * x1 + beta
    cache={}
    cache['x']=x
    cache['mean']=mean
    cache['xhat']=x1
    cache['gamma']=gamma
    cache['ddm']=ddm
    cache['std']=std
    cache['var']=var
    cache['size']=size
    cache['eps']=eps
    
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return out, cache


def spatial_groupnorm_backward(dout, cache):
    """Computes the backward pass for spatial group normalization.

    Inputs:
    - dout: Upstream derivatives, of shape (N, C, H, W)
    - cache: Values from the forward pass

    Returns a tuple of:
    - dx: Gradient with respect to inputs, of shape (N, C, H, W)
    - dgamma: Gradient with respect to scale parameter, of shape (1, C, 1, 1)
    - dbeta: Gradient with respect to shift parameter, of shape (1, C, 1, 1)
    """
    dx, dgamma, dbeta = None, None, None

    ###########################################################################
    # TODO: Implement the backward pass for spatial group normalization.      #
    # This will be extremely similar to the layer norm implementation.        #
    ###########################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    #As per Author [3] , spatial group norm is similar to layer norm with separated into G groups
    #First we invole the cache memory from forward pass
    x=cache['x']
    mean=cache['mean']
    xhat=cache['xhat']
    gamma=cache['gamma']
    std=cache['std']
    size=cache['size']
    ddm=cache['ddm']
    var=cache['var']
    eps=cache['eps']
    N,C,H,W=dout.shape
    #print(x1.shape)
    #we are required to perfrom similar operations as layer norm backward
    dbeta = np.sum(dout, axis=(0,2,3),keepdims=True)#as its 3 dimensional
    #Init dscalx as dout for simplification
    dscalx = dout
    #calculating dgamma wrt dl/dgamma= dl/dy*dy/dgamma
    dgamma = np.sum(dscalx * x1,axis = (0,2,3), keepdims = True)
    #Caculating dbeta wrt dl/db
    dxhat = (gamma * dscalx)
    dxhat=dxhat.reshape(size)
    #We have a series of operations to perfrom
    #Now xhat we know is x-xm/sqrt(var+eps), we perfrom a mul gate on these two as these are branches
    dinvertstd = np.sum(dxhat*ddm.T, axis=1,keepdims=True)
    #calculate gradient wrt 1/sqrt(v+eps)
    ddev_from_mean = dxhat.T* (1./(std))
    # 1/x gate for 1/sqrt(v+eps) = dl/dv*dv/dx
    #dl/dv is previous gate result 
    dstdv = -1/(std**2) * dinvertstd
    #Calculating square root gate now - dl/dsq * dsq/dx
    dvar = (0.5) * 1./std * dstdv
    #Moving to numerator x-xm gate for summation dl/dmu=dl/db*db/dmu
    #The variance of mean is 1/N
    ddev_meansq = (1./N) * np.ones(size).T.dot(dvar)
    #square gate for (x-xm)^2
    ddev_from_mean += 2 * mean * ddev_meansq
    #gradient for x-xm and summation of x is 
    dx = 1 * ddev_from_mean
    dmean = -1 * np.sum(ddev_from_mean, axis=1,keepdims=True)
    #dl/dx=dl/ds*ds/dx for summation of x features
    dx += (1./N) * np.ones(size).T*(dmean)
    dx = dx.reshape(N, C, H, W)
    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################
    return dx, dgamma, dbeta
