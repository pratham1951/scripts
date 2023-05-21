terraform {
  required_providers {
    docker = {
    source = "kreuzwerker/docker"
    version = "3.0.2"
    }
  }
}

provider "docker" {
  host    = "unix:///var/run/docker.sock"
}

resource "docker_image" "nginx" {
    name = "nginx:latest"
    keep_locally = false
  
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name= "nginx-tf"
  ports{
    interal=80
    external=80
  }
}