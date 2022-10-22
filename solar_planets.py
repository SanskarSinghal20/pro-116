
import cv2
from cv2 import FONT_HERSHEY_COMPLEX
img=cv2.imread("solar-system.jpg")


cv2.putText(img,
            "SUN",
            (20,100),
            cv2.FONT_HERSHEY_TRIPLEX,
            3,
            (255,50,20)
            )
            
cv2.putText(img,
            "MERCURY",
            (100,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )
 

cv2.putText(img,
            "VENUS",
            (190,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )

cv2.putText(img,
            "EARTH",
            (290,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )
 
cv2.putText(img,
            "MARS",
            (390,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )

cv2.putText(img,
            "JUPITER",
            (490,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )


cv2.putText(img,
            "SATURN",
            (790,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )

cv2.putText(img,
            "URANUS",
            (990,150),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )

cv2.putText(img,
            "NEPTUNE",
            (1190,190),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (255,250,250)
            )


cv2.imshow('output',img)
cv2.waitKey(0)