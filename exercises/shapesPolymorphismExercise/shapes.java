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