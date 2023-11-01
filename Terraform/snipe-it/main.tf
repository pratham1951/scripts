#Resource Group
resource "azurerm_resource_group" "pratham" {
  name     = "pratham"
  location = var.location
}
#virtual network
resource "azurerm_virtual_network" "pratham-vnet" {
  name                = "pratham-network"
  resource_group_name = azurerm_resource_group.pratham.name
  location            = azurerm_resource_group.pratham.location
  address_space       = ["10.0.0.0/16"]
}

#Subnet
resource "azurerm_subnet" "pratham-subnet" {
  name                 = "pratham-subnet"
  resource_group_name  = azurerm_resource_group.pratham.name
  virtual_network_name = azurerm_virtual_network.pratham-vnet.name
  address_prefixes     = ["10.0.2.0/24"]
}
#Network Interface
resource "azurerm_network_interface" "pratham-main" {
  name                = "pratham-nic"
  location            = azurerm_resource_group.pratham.location
  resource_group_name = azurerm_resource_group.pratham.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.pratham-subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}
#Security Group
resource "azurerm_network_security_group" "pratham-nsg" {
  name                = "my-nsg"
  location            = azurerm_resource_group.pratham.location
  resource_group_name = azurerm_resource_group.pratham.name

  security_rule {
    name                       = "allow-all-traffic"
    priority                   = 200
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_virtual_machine" "pratham" {

  name                  = "pratham-machine"
  location              = azurerm_resource_group.pratham.location
  resource_group_name   = azurerm_resource_group.pratham.name
  network_interface_ids = [azurerm_network_interface.pratham-main.id]
  vm_size               = "Standard_B1s"
 
  storage_os_disk {
    name              = "pratham-osdisk1"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
 # Uncomment this line to delete the OS disk automatically when deleting the VM
  delete_os_disk_on_termination = true

 # Uncomment this line to delete the data disks automatically when deleting the VM
  delete_data_disks_on_termination = true

  storage_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts-gen2"
    version   = "latest"
  }
  os_profile {
    computer_name  = "hostname"
    admin_username      = var.admin_username
    admin_password      = var.admin_password
  }
   os_profile_linux_config {
    disable_password_authentication = false
  }
  
}
