#Bake
<img src="icon.jpg" width="75" height="75">
> The next generation Make..

####What is Bake?
Bake helps you build your project in just on command:
`bake`

####Bake usage:
Bake uses something called a `Bakefile` to build your project.
`Bakefile`'s are simple JSON files.
Heres an example:
```json
//Bakefile
{
	"bake": {
		"task": "task_name",
		"run": [
			"./configure",
			"make install"
		]
	}
}
```
Then just run: `bake`.

####Installation:
Just run these in the command line:
```sh
cd /usr/local
git clone https://github.com/blubrackets/bake
echo 'export PATH=$PATH:/usr/local/bake/bakebin' >> ~/.bash_profile
``` 
Then restart your command line.