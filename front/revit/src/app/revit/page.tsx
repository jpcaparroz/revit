import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";

export default function RevitPage() {
  return (
    <div className="revit">
      <h1>Revit Document AI</h1>
      <p>Welcome to the document analysis section.</p>
      <Link href="/revit-upload" className="upload-button">
        Upload Document
      </Link>
    </div>
  );
}
