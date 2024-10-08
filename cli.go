package main

import (
	"flag"
	"fmt"
	"log"

	"go.bug.st/serial"
	"go.bug.st/serial/enumerator"
)

// Application configuration
type Config struct {
	Alert    bool   // flag
	Warn     bool   // flag
	Notice   bool   // flag
	Debug    bool   // flag
	AppName  string // State: cli app name
	PortName string // State: serial port name
	Color    string // State: color to send
}

// Configure and Open the serial port
func openSerialPort(portName string) (serial.Port, error) {
	// @see https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-linux
	mode := &serial.Mode{
		BaudRate: 115200,
		DataBits: 8,
		StopBits: serial.OneStopBit,
		Parity:   serial.NoParity,
	}

	return serial.Open(portName, mode)
}

// Find the serial port using Enumerator
func findSerialPort(config *Config) error {
	ports, err := enumerator.GetDetailedPortsList()
	if err != nil {
		return err
	}
	if (len(ports)) == 0 {
		return fmt.Errorf("no serial ports found")
	}

	for _, port := range ports {
		if config.Debug {
			log.Printf("Found port: %s\n", port.Name)
		}
		if port.IsUSB {
			if config.Debug {
				log.Printf("  USB ID     %s:%s\n", port.VID, port.PID)
				log.Printf("  USB serial %s\n", port.SerialNumber)
			}
			config.PortName = port.Name
		}
	}

	if config.PortName == "" {
		return fmt.Errorf("no serial port found")
	}
	return nil
}

// Simple flag parser configuration
func parseFlags() Config {
	config := Config{AppName: "xiao-rp2040"}

	flag.BoolVar(&config.Alert, "alert", false, "Display alert color")
	flag.BoolVar(&config.Warn, "warn", false, "Display warn color")
	flag.BoolVar(&config.Notice, "notice", false, "Display notice color")
	flag.BoolVar(&config.Debug, "debug", false, "See debug output")

	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage: %s [options]\n", "serial-test")
		fmt.Fprintf(flag.CommandLine.Output(), "\nNo flags turns off the pulse behavior\n\n")
		flag.PrintDefaults()
	}

	flag.Parse()
	return config
}

// Send the color to the serial port
func sendColor(config Config) error {
	port, err := openSerialPort(config.PortName)
	if err != nil {
		return err
	}

	n, err := port.Write([]byte(fmt.Sprintf("%s\n\r", config.Color))) // serial needs CR+LF to be acknowledged by CircuitPython
	if err != nil {
		return err
	}

	if config.Debug {
		log.Printf("%d bytes written\n", n)
	}
	return nil
}

// configure the correct color
func setColor(config *Config) {
	color := "0"
	switch {
	case config.Alert:
		color = "r"
	case config.Warn:
		color = "y"
	case config.Notice:
		color = "g"
	}
	config.Color = color
}

// A really simple program to interact with the CircuitPython serial console
// on the Adafruit Feather RP2040. A very dumb loop waits for input on the RP2040
// and animates the color to the RGB LED.
func main() {
	config := parseFlags()
	if config.Debug {
		log.SetPrefix(fmt.Sprintf("%s: ", config.AppName))
	}

	err := findSerialPort(&config)
	if err != nil {
		log.Fatal(err)
	}

	setColor(&config)

	err = sendColor(config)
	if err != nil {
		log.Fatal(err)
	}
}
