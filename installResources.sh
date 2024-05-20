#!/bin/bash

if ! command -v pip &> /dev/null
then
    echo "pip nie jest zainstalowany. Zainstaluj pip, zanim uruchomisz ten skrypt."
    exit 1
fi

    "numpy"
    "pandas"
    "scikit-learn"
    "matplotlib"
    "requests"

)

for package in "${packages[@]}"
do
    echo "Instalowanie $package..."
    pip install $package
done

echo "Wszystkie pakiety zostały zainstalowane.
