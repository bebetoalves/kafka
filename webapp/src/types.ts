interface Sensor {
  name: string;
  value: number;
  timestamp: number;
}

interface Analysis {
  name: string;
  min: number;
  max: number;
  avg: number;
  timestamp: number;
}

export type { Sensor, Analysis };
