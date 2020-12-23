import numpy as np

# load_data reads the data and convert the data into a list
def load_data(source_file, total_images, length, width):
    datasetFile = open(source_file)
    data_line = datasetFile.readlines()
    image_data = []

    for i in range(total_images):
        temp_data = []
        for j in range(length * i, length * (i + 1)):
            temp_data.append(data_line[j])
        image_data.append(temp_data)

    return image_data

# load label read the labels and returns a list of labels
def load_label(source_file):
    label_file = open(source_file)
    label_lines = label_file.readlines()
    labels = []
    for i in range(len(label_lines)):
        labels.append(label_lines[i].strip())
    return labels

# The matrix_transformtion is used for converting the list of images_list into list of numpy arrays
def matrix_transformation(image_data, length, width):
    total_data = len(image_data)
    final_data = []

    for i in range(total_data):
        mat = np.zeros((length, width))
        single_image = image_data[i]
        single_image_length = len(single_image)

        for j in range(single_image_length):
            single_line = single_image[j]
            single_line_length = len(single_line)

            for k in range(single_line_length):
                if (single_line[k] == '+' or single_line[k] == '#'):
                    mat[j][k] = 1
        final_data.append(mat)

    return final_data
