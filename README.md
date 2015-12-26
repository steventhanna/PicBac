# PicBac
Automatically back up photos to an external drive

## Purpose
Becuase my Dad was frustrated with the buggy iCloud Photos backup, I created PicBac to automatically back up photos in a given directory to an external hard drive.

PicBac works best nested insidea CRON job, as it allow PicBac to run at a constant interval, whenever the user pleases.

For speed reasons, PicBac only backs up files that meet the following criteria
- The file is one of the following: `png, jpg, jpeg, gif, tiff`
- The file to be backed up is newer than the file on the disk

## Usage
Please note the following lines in `PicBac.py`

```python
# Constants for user to edit
# The source file to scan
source = "EDIT_SOURCE"
# The destination drive to copy
destination = "EDIT_DESTINATION"
```

The `source` variable and the `destination` variable are what should be changed from machine to machine. 
- `source` - the file tree to walk, searcing for images to backup
- `destination` - where the images to be backed up will be copied too

It's pretty straightforward.

