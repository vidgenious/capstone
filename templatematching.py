import cv2
import numpy as np

THRESHOLD = 0.9

# Image path and template path here TODO: Fill paths
image = cv2.imread("")
template = cv2.imread("")

# This results in a plot that compares the similarity
matchPlot = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Compare it to make sure only detections occur where there is a 90% match
match_locations = np.where(matchPlot >= THRESHOLD)

# Populate detections that match
detections = []
for(x, y) in (match_locations[1], match_locations[0]):
    match = {
        "MATCH_VALUE": matchPlot[y, x],
    }

    detections.append(match)

    # Check if no detections for match
    if not bool(detections):
        # run the pause command, error occurred TODO: Pause command
        print("Pause")
