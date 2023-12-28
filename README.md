# meal-plan-generator

Artifact Registry Repo URL: https://us-central1-python.pkg.dev/mealhow/mealhow-python/simple/

```shell
python -m build
twine upload -r  mealhow-python dist/*
pip install --index-url https://us-central1-python.pkg.dev/mealhow/mealhow-python/simple/ mealhow-sdk==0.1.0
```

##Resources:
https://python.plainenglish.io/how-to-store-python-packages-in-google-artifact-registry-9a28d80d8040
https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python38