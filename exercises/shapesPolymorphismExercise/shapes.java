abstract class Shape {
    abstract double getArea();
    abstract double getPerimeter();
}

class Triangle extends Shape {
    double sideA, sideB, sideC, height;

    Triangle(double a, double b, double c, double h) {
        this.sideA = a;
        this.sideB = b;
        this.sideC = c;
        this.height = h;
    }

    double getArea() {
        return (sideA * height) / 2;
    }

    double getPerimeter() {
        return sideA + sideB + sideC;
    }
}

class Square extends Shape {
    double side;

    Square(double side) {
        this.side = side;
    }

    double getArea() {
        return side * side;
    }

    double getPerimeter() {
        return 4 * side;
    }
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    double getArea() {
        return Math.PI * radius * radius;
    }

    double getPerimeter() {
        return 2 * Math.PI * radius; 
    }

    double getRadius() {
        return radius;
    }
}

public class Main {
    public static void main(String[] args) {
        Shape[] shapes = {
            new Triangle(3, 4, 5, 2),
            new Square(4),
            new Circle(3)
        };

        for (Shape shape: shapes) {
            System.out.println("Área: " + shape.getArea());
            System.out.println("Perímetro: " + shape.getPerimeter());

            if (shape instanceof Circle) {
                Circle c = (Circle) shape;
                System.out.println("Raio: " + c.getRadius());
            }

            System.out.println("-----------")
        }
    }
}