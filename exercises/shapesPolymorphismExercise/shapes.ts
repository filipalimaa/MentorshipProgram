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