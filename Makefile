
build: clean gen package runApp

setup: init install

clean:
	rm -rf build && rm -rf dist

init:
	python3 -m venv venv

install:
	bash z-script/install.sh

gen:
	bash z-script/gen.sh

package:
	bash z-script/package.sh

runQtDesigner:
	source venv/bin/activate && pyside2-designer

runApp:
	bash z-script/runApp.sh
