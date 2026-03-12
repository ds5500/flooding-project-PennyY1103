# GIS and remote sensing tutorial
- [applied remote sensing training program](https://arset.unhosting.site/)
	- https://www.earthdata.nasa.gov/data/projects/arset/learn
- GEE textbook
- Sentinel Hub resources
- (optional) [esri academy](https://www.esri.com/training/)
- (optional) The Canada Centre tutorials

# Note - Technical
This section includes all technical notes related to this project. 
## Conda Environment
### conda-forge versus defaults

| \ | defaults | conda-forge |
|---|----------|-------------|
| maintainer | Anaconda, inc. | open-source community|
| package availability | smaller set of packages | much larger ecosystem |
| update speed | slower | faster |
| dependency consistency | packages are built independently. | packages are built in a coordinated ecosystem |

- Q - I have two channels in one environment.yml. Is it common?
	- A - It's common. You may also add `channel_priority: strict` in environment.yml to reduce dependency conflicts or set `conda config --set channel_priority strict` in terminal.
	

