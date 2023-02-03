from pathlib import Path

import image_object


def detect(input_path, output_path, block_size=32):
    """
    Detects an image under a specific directory
    :param input_path: path to input image
    :param output_path: path to output folder
    :param block_size: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    input_path = Path(input_path)
    filename = input_path.name
    output_path = Path(output_path)

    if not input_path.exists():
        print(f"Error: Source Directory \"{str(input_path)}\" did not exist.")
        exit(1)
    elif not output_path.exists():
        print(f"Error: Output Directory \"{str(output_path)}\" did not exist.")
        exit(1)

    single_image = image_object.ImageObject(input_path, filename, output_path, block_size)
    image_result_path = single_image.run()

    print("Done.")
    return image_result_path


if __name__ == "__main__":
    # example script
    # detect('../../dataset/multi_paste/cattle_gcs500_copy_rb5.png', '../../output/', block_size=32)

    detect('../../assets/dataset_example_blur.png', '../../output/', block_size=32)
