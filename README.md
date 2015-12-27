# PicBac
Automatically back up photos to an external drive

## License
Please see the [license](https://github.com/steventhanna/PicBac/blob/master/LICENSE).

## Purpose
Becuase my Dad was frustrated with the buggy iCloud Photos backup, I created PicBac to automatically back up photos in a given directory to an external hard drive.

PicBac works best nested insidea CRON job, as it allow PicBac to run at a constant interval, whenever the user pleases.

For speed reasons, PicBac only backs up files that meet the following criteria
- The file is one of the following: `png, jpg, jpeg, gif, tiff`
- The file to be backed up is newer than the file on the disk

## Installation
First **clone** the project.

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

## Usage
There are two methods that I forsee this being used.

### Manually
Navigate in your preferred CLI to wherever your project is located.

```bash
python PicBac.py
```

### As a CRON Job
**NOTE: I been unable to get custom CRON job's to operate correctly on my machine.  Try below at your own risk.  I am looking into `launchd`**
Although my end user was on OSX, this can be adopted to other Unix canidates

The content below os specific to OSX

#### Open the CRON File
Use your editor of choice... Mine is [Atom](http://atom.io).

```bash
env EDITOR=atom crontab -e
```

where `atom` can be replaced with `vim`, `nano`, `emacs`, etc.

#### Timing Sequence
[**Reference Article**](http://www.techradar.com/us/how-to/computing/apple/terminal-101-creating-cron-jobs-1305651)

The timing sequence of a CRON job looks like this: `* * * * *`
- The first asterisk is for specifying the minute of the run (0-59)
- The second asterisk is for specifying the hour of the run (0-23)
- The third asterisk is for specifying the day of the month for the run (1-31)
- The fourth asterisk is for specifying the month of the run (1-12)
- The fifth asterisk is for specifying the day of the week (where Sunday is equal to 0, up to Saturday is equal to 6)

If you wanted to run the job every day at 1:00pm: `0 13 * * *`

If you wanted the job to run every 30 minutes, you could use the following sequence: `30 * * * *`

And, lastly, if you wanted the job to run once a week on Wednesday, you could type the following sequence: `* * * * 3`

Becuase PicBac only transfers files if the specified path exists, an external drive can be set.  When the external drive is not found, no errors are thrown, it will just try again at the next designated time.

In my Dad's case, I have it configured to run once a day, at 12am. `0 0 * * *`

#### Save CRON File
Save the CRON file per your editors specifications

#### Verify CRON Job
To verify the existance of the CRON job:

```bash
crontab -l
```

## Contributing / Issue's
If you find any issues, please report them on this repo's issue [page](https://github.com/steventhanna/PicBac/issues).

Pull requests to make this software even better are always welcome.
