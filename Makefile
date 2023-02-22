build:
	jb build .

view:
	open _build/html/index.html

import:
	ghp-import -n -p -f _build/html
