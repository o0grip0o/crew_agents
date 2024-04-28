#!/bin/zsh

# variables
model_name="mixtral"
custom_model_name="crewai-mixtral"

# get the base model
ollama pull $model_name

# create the model file
ollama create $custom_model_name -f ./MixtralModelFile

# remove the base model
ollama rm $model_name