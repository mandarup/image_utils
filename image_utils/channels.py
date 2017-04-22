



def apply_threshold(image, thresh=(90, 255)):
    """Threshold a single channel (2d) image."""
    if len(image.shape) != len(thresh):
        raise ValueError('image should be single channel 2d')
    binary = np.zeros_like(image)
    binary[(image > thresh[0]) & (image <= thresh[1])] = 1
    return binary


def get_hls(image):
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    H = hls[:,:,0]
    L = hls[:,:,1]
    S = hls[:,:,2]
    return H, L, S

def get_rgb(image):
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]
    return R, G, B
