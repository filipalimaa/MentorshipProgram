abstract class my_shape {
    abstract get_area(): number;
    abstract get_perimeter(): number;
}

class my_triangle extends my_shape {
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

class my_square extends my_shape {
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

class my_circle extends my_shape {
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

const triangle_ = new my_triangle(2, 4, 5, 2);
const square_ = new my_square(4);
const circle_ = new my_circle(3);

const shapes_: my_shape[] = [triangle_, square_, circle_];

for (const _shape of shapes_) {
    console.log("Area:", _shape.get_area());
    console.log("Perimeter:", _shape.get_perimeter());

    if (_shape instanceof my_circle) {
        console.log("Raio:", _shape.get_radius());
    }
}