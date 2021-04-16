# Download this code intop the 

opencv-examples/objectdetection

## How to use

Use the terminal with ssh login or the XTerm or UXTerm over VNC viewer to run one of the following commands.


### If you use VNC or X11 (e.g. ssh -X pi@...)
In these cases you can run this example with a webcam livestream.

```python peopleCounter.py```


### Comandline only (e.g. ssh pi@...)
If no video screen is avalible we can run these examples with 'noWindow'.
The first 'w' of noWindow needs to be uppercase.

To stop processing new images press CTRL+C. 

```python detect.py noWindow```

to simply classify one image run the following command

```python detect.py ../data/test.jpg```
