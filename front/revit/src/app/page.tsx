import Image from "next/image";
import "./assets/css/index.css";
import Link from "next/link";

export default function HomePage() {

  return (
    <div className="home">

      <div className="title-box">
        <h1 className="title">REVIT</h1>
        <p className="sub-title">loopdevs documents ai</p>
      </div>

      <br />

      <div className="continue-box">
        <Link href="/pages/revit">
          <Image
            src="/images/logo-theme-1.svg"
            className="logo"
            alt="Loopdevs logo"
            width={150}
            height={150}
            />
        </Link>

        <Link href={"/pages/revit"} className="continue">
          click to continue
        </Link>
      </div>
    </div>
  );
}
