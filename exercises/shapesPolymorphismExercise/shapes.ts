abstract class shape {
    abstract get_area(): number;
    abstract get_perimeter(): number;
}

class triangle extends shape {
    side_A: number;
    side_B: number;
    side_C: number;
    height: number;

    constructor(a: number, b: number, c: number, height: number) {
        super();
        this.side_A = a;
        this.side_B = b;
        this.side_C = c;
        this.height = height
    }

    get_area(): number {
        return (this.side_A * this.height) / 2;
    }

    get_perimeter(): number {
        return (this.side_A + this.side_B + this.side_C);
    }
}

class square extends shape {
    side: number;

    constructor(side: number) {
        super();
        this.side = side;
    }

    get_area(): number {
        return this.side * this.side;
    }

    get_perimeter(): number {
        return this.side * 4;
    }
}

class circle extends shape {
    radius: number;

    constructor(radius: number) {
        super();
        this.radius = radius;
    }

    get_area(): number {
        return Math.PI * this.radius * this.radius;
    }

    get_perimeter(): number {
        return 2 * Math.PI * this.radius;
    }

    get_radius(): number {
        return this.radius;
    }
}

const tri = new triangle(2, 4, 5, 2);
const sqr = new square(4);
const crc = new circle(3);

const shapes: shape[] = [tri, sqr, crc];

for (const _shape of shapes) {
    console.log("Area:", _shape.get_area());
    console.log("Perimeter:", _shape.get_perimeter());

    if (_shape instanceof circle) {
        console.log("Raio:", _shape.get_radius());
    }
}