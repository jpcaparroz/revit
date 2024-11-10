import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";
import { LogoTheme1 } from './components/images';


export default function HomePage() {
  return (
    <div className="home">
      <h1>REVIT</h1>
      <p>loopdevs documents ai</p>

      <img src= { LogoTheme1 } alt="Loopdevs logo" />


      <br />

      <Link href={"/revit"}>
        click to continue
      </Link>
    </div>
  );
}
