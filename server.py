"""Main server file.  Calculates SPRs every 15 seconds."""
# External imports
import time
# Internal imports
import SPR

while True:
    SPR.calculateSPRs()
    time.sleep(15)
