#!/bin/zsh

# variables
model_name="mixtral:8x22b"
custom_model_name="crewai-mixtral:8x22b"

# get the base model
ollama pull $model_name

# create the model file
ollama create $custom_model_name -f ./MixtralModelFile

# remove the base model
ollama rm $model_name