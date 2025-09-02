import {
  CanvasPanel,
  LocaleString,
  useVaultSelector,
  useCanvas,
  useManifest,
  useAnnotation,
  useVault,
  SequenceThumbnails,
} from 'react-iiif-vault';
import './App.css';

function App() {
  return (
    <CanvasPanel
      manifest="/yesterdays-lambeth-today/iiif/map-nav.json"
      // manifest="https://digirati-co-uk.github.io/wunder.json"
      // startCanvas="https://digirati-co-uk.github.io/wunder/canvases/3"
      annotations={<RenderAnnotations />}
      pagingEnabled={false}
      header={<ManifestTitle />}
    >
      <SequenceThumbnails classes={{ container: 'thumbs' }} />
      {/* Anything here will have access to the Vault/Manifest/Canvas/Sequence */}
    </CanvasPanel>
  );
}

function ManifestTitle() {
  const manifest = useManifest();
  return <LocaleString>{manifest.label}</LocaleString>;
}

function RenderAnnotations() {
  const canvas = useCanvas();
  const page = canvas.annotations[0];
  const vault = useVault();

  const annotationPage = useVaultSelector(
    (state) => (page?.id ? state.iiif.entities.AnnotationPage[page.id] : null),
    []
  );

  if (!annotationPage) {
    return null;
  }

  // Load the page if its not yet loaded.
  if (!vault.requestStatus(page)) {
    vault.load(page.id);
  }

  return (
    <>
      {annotationPage.items.map((item) => (
        <RenderAnnotation key={item.id} id={item.id} />
      ))}
    </>
  );
}

function RenderAnnotation(props) {
  const annotation = useAnnotation({ id: props.id });
  const targetXYWH = annotation.target.selector.spatial;

  // There are abstractions over this, but this is the raw Atlas components.
  return (
    <world-object {...targetXYWH}>
      <box
        interactive
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();

          // On click logic here.
          console.log('clicked', annotation);
        }}
        relativeStyle
        onMouseLeave={() => {
          // on mouse leave?
        }}
        onMouseEnter={() => {
          // on hover?
        }}
        target={{
          x: 0,
          y: 0,
          width: targetXYWH.width,
          height: targetXYWH.height,
        }}
        style={{
          // styles here
          outline: '1px solid blue',
          backgroundColor: 'rgba(255, 0, 0, .5)',
          ':hover': {
            backgroundColor: 'rgba(0, 255, 0, .5)',
          },
        }}
      />
    </world-object>
  );
}

export default App;
