import subprocess
import getpass


def build_docker_image(image_name, docker_file_path):
    try:
        subprocess.run(['docker', 'build', '-t', image_name, docker_file_path])
    except Exception as e:
        print(e)


def run_docker_container(image_name, container_name, exposed_port=None, application_port=None, run_option=None):
    if run_option == 'web':
        try:
            subprocess.run(['docker', 'run', '-d', '--name', container_name, '-p', exposed_port + ':' + application_port, image_name])
        except Exception as e:
            print(e)
    else:
        subprocess.run(['docker', 'run', '-d', '--name', container_name, image_name])

def start_docker_container(container_name):
    try:
        subprocess.run(['docker', 'start', container_name])
    except Exception as e:
        print(e)

def stop_docker_container(container_name):
    try:
        subprocess.run(['docker', 'stop', container_name])
    except Exception as e:
        print(e)

def remove_docker_container(container_name):
    try:
        subprocess.run(['docker', 'rm', container_name])
    except Exception as e:
        print(e)

def build_multiplatform_docker_image(image_name, docker_file_path):
    try:
        subprocess.run(['docker', 'buildx', 'create', '--name', 'multiarch_builder'])
        subprocess.run(['docker', 'buildx', 'build', '--platform', 'linux/amd64,linux/arm64,linux/arm/v7', '-t', image_name, docker_file_path, '--push'])
    except Exception as e:
        print(e)

def push_docker_image(username, password, image_name):
    try:
        subprocess.run(['docker', 'login', '-u', username, '-p', password])
        subprocess.run(['docker', 'push', image_name])
    except Exception as e:
        print(e)

def create_kubernetes_deployment(image_name, container_name, exposed_port, application_port):
    try:
        subprocess.run(['kubectl', 'create', 'deployment', container_name, '--image', image_name])
        subprocess.run(['kubectl', 'expose', 'deployment', container_name, '--port', exposed_port, '--target-port', application_port])
    except Exception as e:
        print(e)
    
def create_kubernetes_deployment_with_replicas(image_name, container_name, exposed_port, application_port, replicas):
    try:
        subprocess.run(['kubectl', 'create', 'deployment', container_name, '--image', image_name, '--replicas', replicas])
        subprocess.run(['kubectl', 'expose', 'deployment', container_name, '--port', exposed_port, '--target-port', application_port])
    except Exception as e:
        print(e)

def create_kubernetes_service(service_name, container_name, exposed_port, application_port):
    try:
        subprocess.run(['kubectl', 'expose', 'deployment', container_name, '--port', exposed_port, '--target-port', application_port, '--name', service_name])
    except Exception as e:
        print(e)

def menu():
    print('Welcome to docker automation')
    print('1. Build docker image')
    print('2. Run docker container')
    print('3. Start docker container')
    print('4. Stop docker container')
    print('5. Remove docker container')
    print('6. Build multiplatform docker image')
    print('7. Push docker image')
    print('8. Create kubernetes deployment')
    print('9. Create kubernetes deployment with replicas')
    print('10. Create kubernetes service')

    choice = int(input('Enter your choice: '))

    IMAGE_PROMPT = 'Enter image name: '
    CONTAINER_PROMPT = 'Enter container name: '

    if choice == 1:   
        image_name = input(IMAGE_PROMPT)
        docker_file_path = input('Enter docker file path: ')
        build_docker_image(image_name, docker_file_path)
        print(f"Image {image_name} built")
    elif choice == 2:
       run_option = input('Enter run option: ')
       if run_option == 'web':
           image_name = input(IMAGE_PROMPT)
           container_name = input(CONTAINER_PROMPT)
           exposed_port = input('Enter exposed port: ')
           application_port = input('Enter application port: ')
           run_docker_container(image_name, container_name, exposed_port, application_port, run_option)
           print(f"Container {container_name} running on port {exposed_port}")
       else:
           image_name = input(IMAGE_PROMPT)
           container_name = input(CONTAINER_PROMPT)
           run_docker_container(image_name, container_name, run_option)
           print(f"Container {container_name} running")
    elif choice == 3:
        container_name = input(CONTAINER_PROMPT)
        start_docker_container(container_name)
        print(f"Container {container_name} started")
    elif choice == 4:
        container_name = input(CONTAINER_PROMPT)
        stop_docker_container(container_name)
        print(f"Container {container_name} stopped")
    elif choice == 5:
        container_name = input(CONTAINER_PROMPT)
        remove_docker_container(container_name)
        print(f"Container {container_name} removed")
    elif choice == 6:
        image_name = input(IMAGE_PROMPT)
        docker_file_path = input('Enter docker file path: ')
        build_multiplatform_docker_image(image_name, docker_file_path)
        print(f"Image {image_name} built")
    elif choice == 7:
        username = input('Enter username: ')
        password = getpass.getpass('Enter password: ')
        image_name = input(IMAGE_PROMPT)
        push_docker_image(username, password, image_name)
        print(f"Image {image_name} pushed")
    elif choice == 8:
        image_name = input(IMAGE_PROMPT)
        container_name = input(CONTAINER_PROMPT)
        exposed_port = input('Enter exposed port: ')
        application_port = input('Enter application port: ')
        create_kubernetes_deployment(image_name, container_name, exposed_port, application_port)
        print(f"Deployment {container_name} created")
    elif choice == 9:
        image_name = input(IMAGE_PROMPT)
        container_name = input(CONTAINER_PROMPT)
        exposed_port = input('Enter exposed port: ')
        application_port = input('Enter application port: ')
        replicas = input('Enter number of replicas: ')
        create_kubernetes_deployment_with_replicas(image_name, container_name, exposed_port, application_port, replicas)
        print(f"Deployment {container_name} created")

    elif choice == 10:
        service_name = input('Enter service name: ')
        container_name = input(CONTAINER_PROMPT)
        exposed_port = input('Enter exposed port: ')
        application_port = input('Enter application port: ')
        create_kubernetes_service(service_name, container_name, exposed_port, application_port)
        print(f"Service {service_name} created")

    else:
        print('Invalid choice')

if __name__ == '__main__':
    while True:
        menu()
        choice = input('Do you want to continue (y/n): ')
        if choice == 'n':
            break