import Image from "next/image";
import "../../assets/css/revit.css";
import Link from "next/link";
import { useRouter } from 'next/navigation'

export default function RevitPage() {
	const router = useRouter()

	const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		const file = event.target.files ? event.target.files[0] : null;
		if (file) {
			router.push("/pages/revit-upload");
		}
	};

	return (
		<div className="home">

			<Link href="/" className="logo">
				<Image
					src="/images/logo-theme-1.svg"
					alt="Loopdevs logo"
					width={100}
					height={100}
				/>
			</Link>

			<div className="upload-box">
				<input
					type="file"
					id="file-upload"
					accept=".pdf"
					onChange={handleFileChange}
					style={{ display: "none" }}
				/>
				<label htmlFor="file-upload" className="upload-button">
					<Image
						src="/images/upload-icon-theme-1.svg"
						className="upload"
						alt="Upload icon"
						width={80}
						height={80}
					/>
					<div>Upload your <span style={{ fontWeight: 'bold' }}>pdf</span> file</div>
				</label>
			</div>

		</div>
	);
}
