<div align="center">

# `CNF`

<h3>
    CNF Solver
</h3>

<!-- Badges -->
![GitHub Repo stars](https://img.shields.io/github/stars/nemo256/CNF?style=for-the-badge)
![Maintenance](https://shields.io/maintenance/yes/2023?style=for-the-badge)
![License](https://shields.io/github/license/nemo256/CNF?style=for-the-badge)

</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Install 🔨](#install)
* [Use 🚀](#use)
* [License 📑](#license)

## Install 🔨
- Setup a python virtual environment
```shell
$ python -m venv venv
$ source venv/bin/activate
```
- Install packages
```shell
$ pip install -r requirements.txt
```
## Use 🚀
> Use an example:
- Test a CNF e.g (x1 OR x2) AND (x1 or NOT x2)
- Create a clauses.txt file and write the following CNF:
```shell
1 2 0
1 -2 0
3 0
```
- Now run the program:
```shell
$ python CNF.py
```

## License 📑
- Please read [CNF/LICENSE](https://github.com/nemo256/CNF/blob/master/LICENSE)
