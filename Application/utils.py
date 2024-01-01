import numpy as np

# Function to check if a finger is raised
def is_finger_raised(tip, pip, image_height):
    return tip.y * image_height < pip.y * image_height



def find_mask_for_coordinate(masks, coordinate):
    x, y = coordinate

    for mask_index,mask in enumerate(masks):
        mask  =  masks[mask_index,:,:]
        mask_array = np.array(mask)


        # Ensure that the coordinate indices are integers
        x_index = int(x)
        y_index = int(y)

        pixel_value = mask_array[y_index, x_index]
        if pixel_value == 1:
            # Return the index of the mask if the point is inside
            return mask_index  

    return None