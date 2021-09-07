import argparse
import cv2 as cv

parser =argparse.ArgumentParser()
parser.add_argument("path_image_input",help="path to input image to be displayed")

parser.add_argument("path_image_output",help="path of the processed image to be saved")

args = parser.parse_args()

image_input = cv.imread(args.path_image_input)
image_output = cv.imread(args["path_image_input"])

gray_image = cv.cvtColor(image_input, cv.COLOR_BGR2GRAY)

args = vars(parser.parse_args())
cv.imshow("gray image", gray_image)
cv.imshow("loaded image", image_input)
cv.imshow("loaded image2", image_output)

cv.imwrite(args["path_image_output", gray_image])

cv.waitKey(0)
cv.destroyAllWindows()