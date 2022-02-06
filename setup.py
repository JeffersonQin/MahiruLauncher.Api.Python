import setuptools


def read(path):
	with open(path, 'r', encoding='utf-8') as f:
		content = f.read()
	return content


def make_email(prefix, domain):
	return f'{prefix}@{domain}'


setuptools.setup(
	name = 'mahirulauncher-api',
	version = '0.1.2',
	author = 'JeffersonQin',
	author_email = make_email('1247006353', 'qq.com'),
	packages = ['mahiruapi'],
	url = 'https://github.com/JeffersonQin/MahiruLauncher.Api.Python',
	license = 'MIT License',
	description = 'MahiruLauncher API Package for Python',
	long_description = read('README.md'),
	long_description_content_type='text/markdown',
	keywords = ['launcher', 'api', 'scheduler'],
	install_requires = [
		'requests'
	]
)
